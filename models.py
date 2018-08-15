from peewee import *
from config import database


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class Access(BaseModel):
    aid = AutoField()
    mask = CharField()
    status = IntegerField()
    type = CharField()

    class Meta:
        table_name = 'access'


class Actions(BaseModel):
    aid = CharField(primary_key=True)
    callback = CharField()
    description = CharField()
    parameters = TextField()
    type = CharField()

    class Meta:
        table_name = 'actions'


class ActionsAid(BaseModel):
    aid = AutoField()

    class Meta:
        table_name = 'actions_aid'


class Authmap(BaseModel):
    aid = AutoField()
    authname = CharField(unique=True)
    module = CharField()
    uid = IntegerField()

    class Meta:
        table_name = 'authmap'


class BackupMigrateDestinations(BaseModel):
    destination = CharField(column_name='destination_id', primary_key=True)
    location = TextField()
    name = CharField()
    settings = TextField()
    type = CharField()

    class Meta:
        table_name = 'backup_migrate_destinations'


class BackupMigrateProfiles(BaseModel):
    append_timestamp = IntegerField()
    filename = CharField()
    filters = TextField()
    name = CharField()
    profile = CharField(column_name='profile_id', primary_key=True)
    timestamp_format = CharField()

    class Meta:
        table_name = 'backup_migrate_profiles'


class BackupMigrateSchedules(BaseModel):
    cron = IntegerField()
    destination = CharField(column_name='destination_id')
    enabled = IntegerField()
    keep = IntegerField()
    name = CharField()
    period = IntegerField()
    profile = CharField(column_name='profile_id')
    schedule = CharField(column_name='schedule_id', primary_key=True)
    source = CharField(column_name='source_id')

    class Meta:
        table_name = 'backup_migrate_schedules'


class Batch(BaseModel):
    batch = TextField(null=True)
    bid = AutoField()
    timestamp = IntegerField()
    token = CharField(index=True)

    class Meta:
        table_name = 'batch'


class Blocks(BaseModel):
    bid = AutoField()
    cache = IntegerField()
    custom = IntegerField()
    delta = CharField()
    module = CharField()
    pages = TextField()
    region = CharField()
    status = IntegerField()
    theme = CharField()
    throttle = IntegerField()
    title = CharField()
    visibility = IntegerField()
    weight = IntegerField()

    class Meta:
        table_name = 'blocks'
        indexes = (
            (('theme', 'module', 'delta'), True),
            (('theme', 'status', 'region', 'weight', 'module'), False),
        )


class BlocksRoles(BaseModel):
    delta = CharField()
    module = CharField()
    rid = IntegerField(index=True)

    class Meta:
        table_name = 'blocks_roles'
        indexes = (
            (('module', 'delta', 'rid'), True),
        )
        primary_key = CompositeKey('delta', 'module', 'rid')


class Boxes(BaseModel):
    bid = AutoField()
    body = TextField(null=True)
    format = IntegerField()
    info = CharField(unique=True)

    class Meta:
        table_name = 'boxes'


class Cache(BaseModel):
    cid = CharField(primary_key=True)
    created = IntegerField()
    data = TextField(null=True)
    expire = IntegerField(index=True)
    headers = TextField(null=True)
    serialized = IntegerField()

    class Meta:
        table_name = 'cache'


class CacheBlock(BaseModel):
    cid = CharField(primary_key=True)
    created = IntegerField()
    data = TextField(null=True)
    expire = IntegerField(index=True)
    headers = TextField(null=True)
    serialized = IntegerField()

    class Meta:
        table_name = 'cache_block'


class CacheContent(BaseModel):
    cid = CharField(primary_key=True)
    created = IntegerField()
    data = TextField(null=True)
    expire = IntegerField(index=True)
    headers = TextField(null=True)
    serialized = IntegerField()

    class Meta:
        table_name = 'cache_content'


class CacheFilter(BaseModel):
    cid = CharField(primary_key=True)
    created = IntegerField()
    data = TextField(null=True)
    expire = IntegerField(index=True)
    headers = TextField(null=True)
    serialized = IntegerField()

    class Meta:
        table_name = 'cache_filter'


class CacheForm(BaseModel):
    cid = CharField(primary_key=True)
    created = IntegerField()
    data = TextField(null=True)
    expire = IntegerField(index=True)
    headers = TextField(null=True)
    serialized = IntegerField()

    class Meta:
        table_name = 'cache_form'


class CacheMenu(BaseModel):
    cid = CharField(primary_key=True)
    created = IntegerField()
    data = TextField(null=True)
    expire = IntegerField(index=True)
    headers = TextField(null=True)
    serialized = IntegerField()

    class Meta:
        table_name = 'cache_menu'


class CachePage(BaseModel):
    cid = CharField(primary_key=True)
    created = IntegerField()
    data = TextField(null=True)
    expire = IntegerField(index=True)
    headers = TextField(null=True)
    serialized = IntegerField()

    class Meta:
        table_name = 'cache_page'


class CacheUpdate(BaseModel):
    cid = CharField(primary_key=True)
    created = IntegerField()
    data = TextField(null=True)
    expire = IntegerField(index=True)
    headers = TextField(null=True)
    serialized = IntegerField()

    class Meta:
        table_name = 'cache_update'

class CacheViews(BaseModel):
    cid = CharField(primary_key=True)
    created = IntegerField()
    data = TextField(null=True)
    expire = IntegerField(index=True)
    headers = TextField(null=True)
    serialized = IntegerField()

    class Meta:
        table_name = 'cache_views'

class CacheViewsData(BaseModel):
    cid = CharField(primary_key=True)
    created = IntegerField()
    data = TextField(null=True)
    expire = IntegerField(index=True)
    headers = TextField(null=True)
    serialized = IntegerField()

    class Meta:
        table_name = 'cache_views_data'

class Comments(BaseModel):
    cid = AutoField()
    comment = TextField()
    format = IntegerField()
    homepage = CharField(null=True)
    hostname = CharField()
    mail = CharField(null=True)
    name = CharField(null=True)
    nid = IntegerField(index=True)
    pid = IntegerField(index=True)
    status = IntegerField(index=True)
    subject = CharField()
    thread = CharField()
    timestamp = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        table_name = 'comments'

class ConfigPerms(BaseModel):
    machine_name = CharField(unique=True)
    name = CharField()
    path = TextField()
    pid = AutoField()
    status = IntegerField()

    class Meta:
        table_name = 'config_perms'

class ContentFieldEventImage(BaseModel):
    delta = IntegerField()
    field_event_image_data = TextField(null=True)
    field_event_image_fid = IntegerField(null=True)
    field_event_image_list = IntegerField(null=True)
    nid = IntegerField(index=True)
    vid = IntegerField()

    class Meta:
        table_name = 'content_field_event_image'
        indexes = (
            (('vid', 'delta'), True),
        )
        primary_key = CompositeKey('delta', 'vid')

class ContentFieldStoryImage(BaseModel):
    delta = IntegerField()
    field_story_image_data = TextField(null=True)
    field_story_image_fid = IntegerField(null=True)
    field_story_image_list = IntegerField(null=True)
    nid = IntegerField(index=True)
    vid = IntegerField()

    class Meta:
        table_name = 'content_field_story_image'
        indexes = (
            (('vid', 'delta'), True),
        )
        primary_key = CompositeKey('delta', 'vid')

class ContentLock(BaseModel):
    nid = AutoField()
    timestamp = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        table_name = 'content_lock'

class ContentNodeField(BaseModel):
    active = IntegerField()
    db_columns = TextField()
    db_storage = IntegerField()
    field_name = CharField(primary_key=True)
    global_settings = TextField()
    locked = IntegerField()
    module = CharField()
    multiple = IntegerField()
    required = IntegerField()
    type = CharField()

    class Meta:
        table_name = 'content_node_field'

class ContentNodeFieldInstance(BaseModel):
    description = TextField()
    display_settings = TextField()
    field_name = CharField()
    label = CharField()
    type_name = CharField()
    weight = IntegerField()
    widget_active = IntegerField()
    widget_module = CharField()
    widget_settings = TextField()
    widget_type = CharField()

    class Meta:
        table_name = 'content_node_field_instance'
        indexes = (
            (('field_name', 'type_name'), True),
        )
        primary_key = CompositeKey('field_name', 'type_name')

class ContentTypeEvent(BaseModel):
    field_event_datetime_value = DateTimeField(null=True)
    field_event_entry_value = FloatField(null=True)
    field_event_reservation_value = IntegerField(null=True)
    field_event_studentsentry_value = FloatField(null=True)
    nid = IntegerField(index=True)
    vid = AutoField()

    class Meta:
        table_name = 'content_type_event'

class ContentTypeNodeGalleryImage(BaseModel):
    field_node_gallery_image_data = TextField(null=True)
    field_node_gallery_image_fid = IntegerField(null=True)
    field_node_gallery_image_list = IntegerField(null=True)
    nid = IntegerField(index=True)
    vid = AutoField()

    class Meta:
        table_name = 'content_type_node_gallery_image'

class ContentTypeStory(BaseModel):
    nid = IntegerField(index=True)
    vid = AutoField()

    class Meta:
        table_name = 'content_type_story'

class Context(BaseModel):
    condition_mode = IntegerField(null=True)
    conditions = TextField(null=True)
    description = CharField()
    name = CharField(primary_key=True)
    reactions = TextField(null=True)
    tag = CharField()

    class Meta:
        table_name = 'context'

class CtoolsCssCache(BaseModel):
    cid = CharField(primary_key=True)
    css = TextField(null=True)
    filename = CharField(null=True)
    filter = IntegerField(null=True)

    class Meta:
        table_name = 'ctools_css_cache'

class CtoolsObjectCache(BaseModel):
    data = TextField(null=True)
    name = CharField()
    obj = CharField()
    sid = CharField()
    updated = IntegerField(index=True)

    class Meta:
        table_name = 'ctools_object_cache'
        indexes = (
            (('sid', 'obj', 'name'), True),
        )
        primary_key = CompositeKey('name', 'obj', 'sid')

class CustomBreadcrumb(BaseModel):
    bid = AutoField()
    language = CharField(index=True)
    name = CharField(null=True)
    node_type = CharField(null=True)
    paths = CharField(null=True)
    titles = CharField()
    visibility_php = TextField()

    class Meta:
        table_name = 'custom_breadcrumb'
        indexes = (
            (('node_type', 'language'), False),
        )

class CustomBreadcrumbsTaxonomyTerm(BaseModel):
    bid = AutoField()
    language = CharField(index=True)
    name = CharField(null=True)
    paths = CharField(null=True)
    tid = IntegerField()
    titles = CharField()
    visibility_php = TextField()

    class Meta:
        table_name = 'custom_breadcrumbs_taxonomy_term'
        indexes = (
            (('tid', 'language'), False),
        )

class CustomBreadcrumbsTaxonomyVocabulary(BaseModel):
    bid = AutoField()
    language = CharField(index=True)
    name = CharField(null=True)
    paths = CharField(null=True)
    titles = CharField()
    vid = IntegerField()
    visibility_php = TextField()

    class Meta:
        table_name = 'custom_breadcrumbs_taxonomy_vocabulary'
        indexes = (
            (('vid', 'language'), False),
        )

class DateFormatLocale(BaseModel):
    format = CharField()
    language = CharField()
    type = CharField()

    class Meta:
        table_name = 'date_format_locale'
        indexes = (
            (('type', 'language'), True),
        )
        primary_key = CompositeKey('language', 'type')

class DateFormatTypes(BaseModel):
    locked = IntegerField()
    title = CharField()
    type = CharField(primary_key=True)

    class Meta:
        table_name = 'date_format_types'

class DateFormats(BaseModel):
    dfid = AutoField()
    format = CharField()
    locked = IntegerField()
    type = CharField()

    class Meta:
        table_name = 'date_formats'
        indexes = (
            (('format', 'type'), True),
        )

class DevelQueries(BaseModel):
    function = CharField()
    hash = CharField(primary_key=True)
    qid = IntegerField(index=True)
    query = TextField()

    class Meta:
        table_name = 'devel_queries'

class DevelTimes(BaseModel):
    qid = IntegerField(index=True)
    tid = AutoField()
    time = FloatField(null=True)

    class Meta:
        table_name = 'devel_times'

class Files(BaseModel):
    fid = AutoField()
    filemime = CharField()
    filename = CharField()
    filepath = CharField()
    filesize = IntegerField()
    status = IntegerField(index=True)
    timestamp = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        table_name = 'files'

class FilterFormats(BaseModel):
    cache = IntegerField()
    format = AutoField()
    name = CharField(unique=True)
    roles = CharField()

    class Meta:
        table_name = 'filter_formats'

class Filters(BaseModel):
    delta = IntegerField()
    fid = AutoField()
    format = IntegerField()
    module = CharField()
    weight = IntegerField()

    class Meta:
        table_name = 'filters'
        indexes = (
            (('format', 'module', 'delta'), True),
            (('format', 'weight', 'module', 'delta'), False),
        )

class Flood(BaseModel):
    event = CharField()
    fid = AutoField()
    hostname = CharField()
    timestamp = IntegerField()

    class Meta:
        table_name = 'flood'
        indexes = (
            (('event', 'hostname', 'timestamp'), False),
        )

class History(BaseModel):
    nid = IntegerField(index=True)
    timestamp = IntegerField()
    uid = IntegerField()

    class Meta:
        table_name = 'history'
        indexes = (
            (('uid', 'nid'), True),
        )
        primary_key = CompositeKey('nid', 'uid')

class I18NBlocks(BaseModel):
    delta = CharField()
    ibid = AutoField()
    language = CharField()
    module = CharField()
    type = IntegerField()

    class Meta:
        table_name = 'i18n_blocks'

class I18NStrings(BaseModel):
    format = IntegerField()
    lid = AutoField()
    objectid = CharField()
    objectindex = IntegerField()
    property = CharField()
    type = CharField()

    class Meta:
        table_name = 'i18n_strings'

class I18NVariable(BaseModel):
    language = CharField()
    name = CharField()
    value = TextField()

    class Meta:
        table_name = 'i18n_variable'
        indexes = (
            (('name', 'language'), True),
        )
        primary_key = CompositeKey('language', 'name')

class ImagecacheAction(BaseModel):
    action = CharField()
    actionid = AutoField()
    data = TextField()
    module = CharField()
    presetid = IntegerField(index=True)
    weight = IntegerField()

    class Meta:
        table_name = 'imagecache_action'

class ImagecachePreset(BaseModel):
    presetid = AutoField()
    presetname = CharField()

    class Meta:
        table_name = 'imagecache_preset'

class ImceFiles(BaseModel):
    fid = AutoField()

    class Meta:
        table_name = 'imce_files'

class Languages(BaseModel):
    direction = IntegerField()
    domain = CharField()
    enabled = IntegerField()
    formula = CharField()
    javascript = CharField()
    language = CharField(primary_key=True)
    name = CharField()
    native = CharField()
    plurals = IntegerField()
    prefix = CharField()
    weight = IntegerField()

    class Meta:
        table_name = 'languages'
        indexes = (
            (('weight', 'name'), False),
        )

class LocalesSource(BaseModel):
    lid = AutoField()
    location = CharField()
    source = TextField(index=True)
    textgroup = CharField()
    version = CharField()

    class Meta:
        table_name = 'locales_source'
        indexes = (
            (('textgroup', 'location'), False),
        )

class LocalesTarget(BaseModel):
    i18n_status = IntegerField()
    language = CharField()
    lid = IntegerField(index=True)
    plid = IntegerField(index=True)
    plural = IntegerField(index=True)
    translation = TextField()

    class Meta:
        table_name = 'locales_target'
        indexes = (
            (('language', 'lid', 'plural'), True),
        )
        primary_key = CompositeKey('language', 'lid', 'plural')

class MenuCustom(BaseModel):
    description = TextField(null=True)
    menu_name = CharField(primary_key=True)
    title = CharField()

    class Meta:
        table_name = 'menu_custom'

class MenuLinks(BaseModel):
    customized = IntegerField()
    depth = IntegerField()
    expanded = IntegerField()
    external = IntegerField()
    has_children = IntegerField()
    hidden = IntegerField()
    link_path = CharField()
    link_title = CharField()
    menu_name = CharField()
    mlid = AutoField()
    module = CharField()
    options = TextField(null=True)
    p1 = IntegerField()
    p2 = IntegerField()
    p3 = IntegerField()
    p4 = IntegerField()
    p5 = IntegerField()
    p6 = IntegerField()
    p7 = IntegerField()
    p8 = IntegerField()
    p9 = IntegerField()
    plid = IntegerField()
    router_path = CharField(index=True)
    updated = IntegerField()
    weight = IntegerField()

    class Meta:
        table_name = 'menu_links'
        indexes = (
            (('link_path', 'menu_name'), False),
            (('menu_name', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9'), False),
            (('menu_name', 'plid', 'expanded', 'has_children'), False),
        )

class MenuRouter(BaseModel):
    access_arguments = TextField(null=True)
    access_callback = CharField()
    block_callback = CharField()
    description = TextField()
    file = TextField(null=True)
    fit = IntegerField(index=True)
    load_functions = TextField()
    number_parts = IntegerField()
    page_arguments = TextField(null=True)
    page_callback = CharField()
    path = CharField(primary_key=True)
    position = CharField()
    tab_parent = CharField(index=True)
    tab_root = CharField()
    title = CharField()
    title_arguments = CharField()
    title_callback = CharField()
    to_arg_functions = TextField()
    type = IntegerField()
    weight = IntegerField()

    class Meta:
        table_name = 'menu_router'
        indexes = (
            (('tab_root', 'weight', 'title'), False),
        )

class Node(BaseModel):
    changed = IntegerField(index=True)
    comment = IntegerField()
    created = IntegerField(index=True)
    language = CharField()
    moderate = IntegerField(index=True)
    nid = AutoField()
    promote = IntegerField()
    status = IntegerField()
    sticky = IntegerField()
    title = CharField()
    tnid = IntegerField(index=True)
    translate = IntegerField(index=True)
    type = CharField(index=True)
    uid = IntegerField(index=True)
    vid = IntegerField(unique=True)

    class Meta:
        table_name = 'node'
        indexes = (
            (('promote', 'status'), False),
            (('status', 'type', 'nid'), False),
            (('title', 'type'), False),
        )

class NodeAccess(BaseModel):
    gid = IntegerField()
    grant_delete = IntegerField()
    grant_update = IntegerField()
    grant_view = IntegerField()
    nid = IntegerField()
    realm = CharField()

    class Meta:
        table_name = 'node_access'
        indexes = (
            (('nid', 'gid', 'realm'), True),
        )
        primary_key = CompositeKey('gid', 'nid', 'realm')

class NodeCommentStatistics(BaseModel):
    comment_count = IntegerField(index=True)
    last_comment_name = CharField(null=True)
    last_comment_timestamp = IntegerField(index=True)
    last_comment_uid = IntegerField(index=True)
    nid = AutoField()

    class Meta:
        table_name = 'node_comment_statistics'

class NodeCounter(BaseModel):
    daycount = IntegerField()
    nid = AutoField()
    timestamp = IntegerField()
    totalcount = BigIntegerField()

    class Meta:
        table_name = 'node_counter'

class NodeGalleryGalleries(BaseModel):
    cover_image = IntegerField(null=True, unique=True)
    gid = AutoField()
    img_count = IntegerField(index=True)
    pub_img_count = IntegerField(index=True)

    class Meta:
        table_name = 'node_gallery_galleries'

class NodeGalleryImages(BaseModel):
    gid = IntegerField(index=True)
    nid = AutoField()
    weight = IntegerField()

    class Meta:
        table_name = 'node_gallery_images'

class NodeGalleryRelationships(BaseModel):
    gallery_type = CharField()
    image_type = CharField()
    imagefield_name = CharField()
    rid = AutoField()
    settings = TextField(null=True)

    class Meta:
        table_name = 'node_gallery_relationships'

class NodeRevisions(BaseModel):
    body = TextField()
    format = IntegerField()
    log = TextField()
    nid = IntegerField(index=True)
    teaser = TextField()
    timestamp = IntegerField()
    title = CharField()
    uid = IntegerField(index=True)
    vid = AutoField()

    class Meta:
        table_name = 'node_revisions'

class NodeType(BaseModel):
    body_label = CharField()
    custom = IntegerField()
    description = TextField()
    has_body = IntegerField()
    has_title = IntegerField()
    help = TextField()
    locked = IntegerField()
    min_word_count = IntegerField()
    modified = IntegerField()
    module = CharField()
    name = CharField()
    orig_type = CharField()
    title_label = CharField()
    type = CharField(primary_key=True)

    class Meta:
        table_name = 'node_type'

class Nodewords(BaseModel):
    content = TextField()
    id = IntegerField()
    mtid = AutoField()
    name = CharField(index=True)
    type = IntegerField()

    class Meta:
        table_name = 'nodewords'
        indexes = (
            (('type', 'id'), False),
            (('type', 'id', 'name'), True),
        )

class NodewordsCustom(BaseModel):
    enabled = IntegerField()
    name = CharField()
    path = TextField()
    pid = AutoField()
    weight = IntegerField()

    class Meta:
        table_name = 'nodewords_custom'

class PageTitle(BaseModel):
    id = IntegerField()
    page_title = CharField()
    type = CharField()

    class Meta:
        table_name = 'page_title'
        indexes = (
            (('type', 'id'), True),
        )
        primary_key = CompositeKey('id', 'type')

class PathRedirect(BaseModel):
    fragment = CharField(null=True)
    language = CharField()
    last_used = IntegerField()
    query = CharField(null=True)
    redirect = CharField()
    rid = AutoField()
    source = CharField()
    type = IntegerField()

    class Meta:
        table_name = 'path_redirect'
        indexes = (
            (('source', 'language'), True),
        )

class Permission(BaseModel):
    perm = TextField(null=True)
    pid = AutoField()
    rid = IntegerField(index=True)
    tid = IntegerField()

    class Meta:
        table_name = 'permission'

class Role(BaseModel):
    name = CharField(unique=True)
    rid = AutoField()

    class Meta:
        table_name = 'role'

class Scheduler(BaseModel):
    nid = AutoField()
    publish_on = IntegerField(index=True)
    unpublish_on = IntegerField(index=True)

    class Meta:
        table_name = 'scheduler'

class SearchDataset(BaseModel):
    data = TextField()
    reindex = IntegerField()
    sid = IntegerField()
    type = CharField(null=True)

    class Meta:
        table_name = 'search_dataset'
        indexes = (
            (('sid', 'type'), True),
        )
        primary_key = False

class SearchIndex(BaseModel):
    score = FloatField(null=True)
    sid = IntegerField()
    type = CharField(null=True)
    word = CharField(index=True)

    class Meta:
        table_name = 'search_index'
        indexes = (
            (('sid', 'type'), False),
            (('word', 'sid', 'type'), True),
        )
        primary_key = False

class SearchNodeLinks(BaseModel):
    caption = TextField(null=True)
    nid = IntegerField(index=True)
    sid = IntegerField()
    type = CharField()

    class Meta:
        table_name = 'search_node_links'
        indexes = (
            (('sid', 'type', 'nid'), True),
        )
        primary_key = CompositeKey('nid', 'sid', 'type')

class SearchTotal(BaseModel):
    count = FloatField(null=True)
    word = CharField(primary_key=True)

    class Meta:
        table_name = 'search_total'

class Semaphore(BaseModel):
    expire = FloatField(index=True)
    name = CharField(primary_key=True)
    value = CharField()

    class Meta:
        table_name = 'semaphore'

class Sessions(BaseModel):
    cache = IntegerField()
    hostname = CharField()
    session = TextField(null=True)
    sid = CharField(primary_key=True)
    timestamp = IntegerField(index=True)
    uid = IntegerField(index=True)

    class Meta:
        table_name = 'sessions'

class System(BaseModel):
    bootstrap = IntegerField()
    filename = CharField(primary_key=True)
    info = TextField(null=True)
    name = CharField()
    owner = CharField()
    schema_version = IntegerField()
    status = IntegerField()
    throttle = IntegerField()
    type = CharField()
    weight = IntegerField()

    class Meta:
        table_name = 'system'
        indexes = (
            (('type', 'name'), False),
            (('type', 'status', 'bootstrap', 'weight', 'filename'), False),
            (('type', 'status', 'weight', 'filename'), False),
        )

class TermData(BaseModel):
    description = TextField(null=True)
    language = CharField()
    name = CharField()
    tid = AutoField()
    trid = IntegerField()
    vid = IntegerField()
    weight = IntegerField()

    class Meta:
        table_name = 'term_data'
        indexes = (
            (('vid', 'name'), False),
            (('vid', 'weight', 'name'), False),
        )

class TermHierarchy(BaseModel):
    parent = IntegerField(index=True)
    tid = IntegerField()

    class Meta:
        table_name = 'term_hierarchy'
        indexes = (
            (('tid', 'parent'), True),
        )
        primary_key = CompositeKey('parent', 'tid')

class TermNode(BaseModel):
    nid = IntegerField(index=True)
    tid = IntegerField()
    vid = IntegerField(index=True)

    class Meta:
        table_name = 'term_node'
        indexes = (
            (('tid', 'vid'), True),
        )
        primary_key = CompositeKey('tid', 'vid')

class TermRelation(BaseModel):
    tid1 = IntegerField()
    tid2 = IntegerField(index=True)
    trid = AutoField()

    class Meta:
        table_name = 'term_relation'
        indexes = (
            (('tid1', 'tid2'), True),
        )

class TermSynonym(BaseModel):
    name = CharField()
    tid = IntegerField(index=True)
    tsid = AutoField()

    class Meta:
        table_name = 'term_synonym'
        indexes = (
            (('name', 'tid'), False),
        )

class UrlAlias(BaseModel):
    dst = CharField()
    language = CharField()
    pid = AutoField()
    src = CharField()

    class Meta:
        table_name = 'url_alias'
        indexes = (
            (('dst', 'language', 'pid'), True),
            (('src', 'language', 'pid'), False),
        )

class Users(BaseModel):
    access = IntegerField(index=True)
    created = IntegerField(index=True)
    data = TextField(null=True)
    init = CharField(null=True)
    language = CharField()
    login = IntegerField()
    mail = CharField(index=True, null=True)
    mode = IntegerField()
    name = CharField(unique=True)
    pass_ = CharField(column_name='pass')
    picture = CharField()
    signature = CharField()
    signature_format = IntegerField()
    sort = IntegerField(null=True)
    status = IntegerField()
    theme = CharField()
    threshold = IntegerField(null=True)
    timezone = CharField(null=True)
    timezone_name = CharField()
    uid = AutoField()

    class Meta:
        table_name = 'users'

class UsersRoles(BaseModel):
    rid = IntegerField(index=True)
    uid = IntegerField()

    class Meta:
        table_name = 'users_roles'
        indexes = (
            (('uid', 'rid'), True),
        )
        primary_key = CompositeKey('rid', 'uid')

class Variable(BaseModel):
    name = CharField(primary_key=True)
    value = TextField()

    class Meta:
        table_name = 'variable'

class ViewsDisplay(BaseModel):
    display_options = TextField(null=True)
    display_plugin = CharField()
    display_title = CharField()
    id = CharField()
    position = IntegerField(null=True)
    vid = IntegerField()

    class Meta:
        table_name = 'views_display'
        indexes = (
            (('vid', 'id'), True),
            (('vid', 'position'), False),
        )
        primary_key = CompositeKey('id', 'vid')

class ViewsObjectCache(BaseModel):
    data = TextField(null=True)
    name = CharField(null=True)
    obj = CharField(null=True)
    sid = CharField(null=True)
    updated = IntegerField(index=True)

    class Meta:
        table_name = 'views_object_cache'
        indexes = (
            (('sid', 'obj', 'name'), False),
        )
        primary_key = False

class ViewsView(BaseModel):
    base_table = CharField()
    core = IntegerField(null=True)
    description = CharField(null=True)
    name = CharField(unique=True)
    tag = CharField(null=True)
    vid = AutoField()

    class Meta:
        table_name = 'views_view'

class Vocabulary(BaseModel):
    description = TextField(null=True)
    help = CharField()
    hierarchy = IntegerField()
    language = CharField()
    module = CharField()
    multiple = IntegerField()
    name = CharField()
    relations = IntegerField()
    required = IntegerField()
    tags = IntegerField()
    vid = AutoField()
    weight = IntegerField()

    class Meta:
        table_name = 'vocabulary'
        indexes = (
            (('weight', 'name'), False),
        )

class VocabularyNodeTypes(BaseModel):
    type = CharField()
    vid = IntegerField(index=True)

    class Meta:
        table_name = 'vocabulary_node_types'
        indexes = (
            (('type', 'vid'), True),
        )
        primary_key = CompositeKey('type', 'vid')

class Watchdog(BaseModel):
    hostname = CharField()
    link = CharField()
    location = TextField()
    message = TextField()
    referer = TextField(null=True)
    severity = IntegerField()
    timestamp = IntegerField()
    type = CharField(index=True)
    uid = IntegerField()
    variables = TextField()
    wid = AutoField()

    class Meta:
        table_name = 'watchdog'

class Webform(BaseModel):
    additional_submit = TextField(null=True)
    additional_validate = TextField(null=True)
    allow_draft = IntegerField()
    auto_save = IntegerField()
    block = IntegerField()
    confirmation = TextField()
    confirmation_format = IntegerField()
    nid = AutoField()
    redirect_url = CharField(null=True)
    status = IntegerField()
    submit_interval = IntegerField()
    submit_limit = IntegerField()
    submit_notice = IntegerField()
    submit_text = CharField(null=True)
    teaser = IntegerField()
    total_submit_interval = IntegerField()
    total_submit_limit = IntegerField()

    class Meta:
        table_name = 'webform'

class WebformComponent(BaseModel):
    cid = IntegerField()
    extra = TextField()
    form_key = CharField(null=True)
    mandatory = IntegerField()
    name = CharField(null=True)
    nid = IntegerField()
    pid = IntegerField()
    type = CharField(null=True)
    value = TextField()
    weight = IntegerField()

    class Meta:
        table_name = 'webform_component'
        indexes = (
            (('nid', 'cid'), True),
        )
        primary_key = CompositeKey('cid', 'nid')

class WebformEmails(BaseModel):
    attachments = IntegerField()
    eid = IntegerField()
    email = TextField(null=True)
    excluded_components = TextField()
    from_address = CharField(null=True)
    from_name = CharField(null=True)
    html = IntegerField()
    nid = IntegerField()
    subject = CharField(null=True)
    template = TextField(null=True)

    class Meta:
        table_name = 'webform_emails'
        indexes = (
            (('nid', 'eid'), True),
        )
        primary_key = CompositeKey('eid', 'nid')

class WebformLastDownload(BaseModel):
    nid = IntegerField()
    requested = IntegerField()
    sid = IntegerField()
    uid = IntegerField()

    class Meta:
        table_name = 'webform_last_download'
        indexes = (
            (('nid', 'uid'), True),
        )
        primary_key = CompositeKey('nid', 'uid')

class WebformRoles(BaseModel):
    nid = IntegerField()
    rid = IntegerField()

    class Meta:
        table_name = 'webform_roles'
        indexes = (
            (('nid', 'rid'), True),
        )
        primary_key = CompositeKey('nid', 'rid')

class WebformSubmissions(BaseModel):
    is_draft = IntegerField()
    nid = IntegerField()
    remote_addr = CharField(null=True)
    sid = AutoField()
    submitted = IntegerField()
    uid = IntegerField()

    class Meta:
        table_name = 'webform_submissions'
        indexes = (
            (('nid', 'sid'), False),
            (('nid', 'uid', 'sid'), False),
            (('sid', 'nid'), True),
        )

class WebformSubmittedData(BaseModel):
    cid = IntegerField()
    data = TextField()
    nid = IntegerField(index=True)
    no = CharField()
    sid = IntegerField()

    class Meta:
        table_name = 'webform_submitted_data'
        indexes = (
            (('nid', 'sid', 'cid', 'no'), True),
            (('sid', 'nid'), False),
        )
        primary_key = CompositeKey('cid', 'nid', 'no', 'sid')

class Wysiwyg(BaseModel):
    editor = CharField()
    format = AutoField()
    settings = TextField(null=True)

    class Meta:
        table_name = 'wysiwyg'

class WysiwygUser(BaseModel):
    format = IntegerField(index=True, null=True)
    status = IntegerField()
    uid = IntegerField(index=True)

    class Meta:
        table_name = 'wysiwyg_user'
        primary_key = False

class Xmlsitemap(BaseModel):
    access = IntegerField()
    changecount = IntegerField()
    changefreq = IntegerField()
    id = IntegerField()
    language = CharField(index=True)
    lastmod = IntegerField()
    loc = CharField(index=True)
    priority = FloatField(null=True)
    priority_override = IntegerField()
    status = IntegerField()
    status_override = IntegerField()
    subtype = CharField()
    type = CharField()

    class Meta:
        table_name = 'xmlsitemap'
        indexes = (
            (('access', 'status', 'loc'), False),
            (('id', 'type'), True),
            (('type', 'subtype'), False),
        )
        primary_key = CompositeKey('id', 'type')

class XmlsitemapSitemap(BaseModel):
    chunks = IntegerField()
    context = TextField()
    links = IntegerField()
    max_filesize = IntegerField()
    smid = CharField(primary_key=True)
    updated = IntegerField()

    class Meta:
        table_name = 'xmlsitemap_sitemap'

