import csv
import models


def migrate_events():
    query = models.Node.select(
        models.Node.title,
        models.Node.language,
        models.Node.nid,
        models.Node.created,
        models.NodeRevisions.body).join(
            models.NodeRevisions, on=(models.Node.nid == models.NodeRevisions.nid)
    ).where(
        models.Node.type == 'event', models.Node.status == 1
    ).order_by(
        models.Node.created.desc()
    )
    taxonomies = get_taxonomies()
    fields = get_content_type_fields()
    images = get_event_images()
    with open('events.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='~', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            ['title', 'lang', 'featured image', 'datetime published', 'datetime event',
             'price', 'categories', 'content']
        )
        for node in query:
            try:
                content = node.noderevisions.body.replace('\n', '').replace('\r', '')
                writer.writerow([
                    node.title,
                    node.language,
                    'https://a4.sk/' + images[node.nid].files.filepath,
                    node.created,
                    fields[node.nid].field_event_datetime_value,
                    fields[node.nid].field_event_entry_value,
                    taxonomies[node.nid], content]
                )
            except:
                pass


def migrate_stories():
    query = models.Node.select(
        models.Node.title,
        models.Node.language,
        models.Node.nid,
        models.Node.created,
        models.NodeRevisions.body).join(
        models.NodeRevisions, on=(models.Node.nid == models.NodeRevisions.nid)
    ).where(
        models.Node.type == 'story', models.Node.status == 1
    ).order_by(
        models.Node.created.desc()
    )
    taxonomies = get_taxonomies()
    images = get_story_images()
    with open('stories.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='~', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            ['title', 'lang', 'featured image', 'datetime published', 'categories', 'content']
        )
        for node in query:
            try:
                content = node.noderevisions.body.replace('\n', '').replace('\r', '')
                writer.writerow([
                    node.title,
                    node.language,
                    'https://a4.sk/' + images[node.nid].files.filepath,
                    node.created,
                    taxonomies[node.nid],
                    content]
                )
            except:
                pass


def get_taxonomies():
    query = models.TermNode.select(
        models.TermNode.nid, models.fn.group_concat(models.TermData.name).alias('test')).join(
        models.TermData, on=(models.TermNode.tid == models.TermData.tid)
    ).group_by(models.TermNode.nid)
    return {node.nid: node.test for node in query}


def get_content_type_fields():
    query = models.ContentTypeEvent.select()
    return {node.nid: node for node in query}


def get_story_images():
    query = models.ContentFieldStoryImage.select(
        models.ContentFieldStoryImage.nid, models.Files.filepath).join(
        models.Files, on=(models.ContentFieldStoryImage.field_story_image_fid == models.Files.fid)
    )
    return {node.nid: node for node in query}


def get_event_images():
    query = models.ContentFieldEventImage.select(
        models.ContentFieldEventImage.nid, models.Files.filepath).join(
        models.Files, on=(models.ContentFieldEventImage.field_event_image_fid == models.Files.fid)
    )
    return {node.nid: node for node in query}


if __name__ == '__main__':
    migrate_events()
    migrate_stories()
