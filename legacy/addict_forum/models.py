# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Phpbb3AclGroups(models.Model):
    group_id = models.IntegerField()
    forum_id = models.IntegerField()
    auth_option_id = models.IntegerField()
    auth_role_id = models.IntegerField()
    auth_setting = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_acl_groups'


class Phpbb3AclOptions(models.Model):
    auth_option_id = models.IntegerField(primary_key=True)
    auth_option = models.CharField(max_length=50)
    is_global = models.IntegerField()
    is_local = models.IntegerField()
    founder_only = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_acl_options'


class Phpbb3AclRoles(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=255)
    role_description = models.TextField()
    role_type = models.CharField(max_length=10)
    role_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_acl_roles'


class Phpbb3AclRolesData(models.Model):
    role_id = models.IntegerField()
    auth_option_id = models.IntegerField()
    auth_setting = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_acl_roles_data'


class Phpbb3AclUsers(models.Model):
    user_id = models.IntegerField()
    forum_id = models.IntegerField()
    auth_option_id = models.IntegerField()
    auth_role_id = models.IntegerField()
    auth_setting = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_acl_users'


class Phpbb3Attachments(models.Model):
    attach_id = models.IntegerField(primary_key=True)
    post_msg_id = models.IntegerField()
    topic_id = models.IntegerField()
    in_message = models.IntegerField()
    poster_id = models.IntegerField()
    is_orphan = models.IntegerField()
    physical_filename = models.CharField(max_length=255)
    real_filename = models.CharField(max_length=255)
    download_count = models.IntegerField()
    attach_comment = models.TextField()
    extension = models.CharField(max_length=100)
    mimetype = models.CharField(max_length=100)
    filesize = models.IntegerField()
    filetime = models.IntegerField()
    thumbnail = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_attachments'


class Phpbb3Banlist(models.Model):
    ban_id = models.IntegerField(primary_key=True)
    ban_userid = models.IntegerField()
    ban_ip = models.CharField(max_length=40)
    ban_email = models.CharField(max_length=100)
    ban_start = models.IntegerField()
    ban_end = models.IntegerField()
    ban_exclude = models.IntegerField()
    ban_reason = models.CharField(max_length=255)
    ban_give_reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'phpbb3_banlist'


class Phpbb3Bbcodes(models.Model):
    bbcode_id = models.IntegerField(primary_key=True)
    bbcode_tag = models.CharField(max_length=16)
    bbcode_helpline = models.CharField(max_length=255)
    display_on_posting = models.IntegerField()
    bbcode_match = models.TextField()
    bbcode_tpl = models.TextField()
    first_pass_match = models.TextField()
    first_pass_replace = models.TextField()
    second_pass_match = models.TextField()
    second_pass_replace = models.TextField()

    class Meta:
        managed = False
        db_table = 'phpbb3_bbcodes'


class Phpbb3Bookmarks(models.Model):
    topic_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_bookmarks'


class Phpbb3Bots(models.Model):
    bot_id = models.IntegerField(primary_key=True)
    bot_active = models.IntegerField()
    bot_name = models.CharField(max_length=255)
    user_id = models.IntegerField()
    bot_agent = models.CharField(max_length=255)
    bot_ip = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'phpbb3_bots'


class Phpbb3Config(models.Model):
    config_name = models.CharField(primary_key=True, max_length=255)
    config_value = models.CharField(max_length=255)
    is_dynamic = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_config'


class Phpbb3Confirm(models.Model):
    confirm_id = models.CharField(max_length=32)
    session_id = models.CharField(max_length=32)
    confirm_type = models.IntegerField()
    code = models.CharField(max_length=8)
    seed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_confirm'


class Phpbb3Disallow(models.Model):
    disallow_id = models.IntegerField(primary_key=True)
    disallow_username = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'phpbb3_disallow'


class Phpbb3Drafts(models.Model):
    draft_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    topic_id = models.IntegerField()
    forum_id = models.IntegerField()
    save_time = models.IntegerField()
    draft_subject = models.CharField(max_length=100)
    draft_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'phpbb3_drafts'


class Phpbb3ExtensionGroups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=255)
    cat_id = models.IntegerField()
    allow_group = models.IntegerField()
    download_mode = models.IntegerField()
    upload_icon = models.CharField(max_length=255)
    max_filesize = models.IntegerField()
    allowed_forums = models.TextField()
    allow_in_pm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_extension_groups'


class Phpbb3Extensions(models.Model):
    extension_id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    extension = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'phpbb3_extensions'


class Phpbb3Forums(models.Model):
    forum_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    left_id = models.IntegerField()
    right_id = models.IntegerField()
    forum_parents = models.TextField()
    forum_name = models.CharField(max_length=255)
    forum_desc = models.TextField()
    forum_desc_bitfield = models.CharField(max_length=255)
    forum_desc_options = models.IntegerField()
    forum_desc_uid = models.CharField(max_length=8)
    forum_link = models.CharField(max_length=255)
    forum_password = models.CharField(max_length=40)
    forum_style = models.IntegerField()
    forum_image = models.CharField(max_length=255)
    forum_rules = models.TextField()
    forum_rules_link = models.CharField(max_length=255)
    forum_rules_bitfield = models.CharField(max_length=255)
    forum_rules_options = models.IntegerField()
    forum_rules_uid = models.CharField(max_length=8)
    forum_topics_per_page = models.IntegerField()
    forum_type = models.IntegerField()
    forum_status = models.IntegerField()
    forum_posts = models.IntegerField()
    forum_topics = models.IntegerField()
    forum_topics_real = models.IntegerField()
    forum_last_post_id = models.IntegerField()
    forum_last_poster_id = models.IntegerField()
    forum_last_post_subject = models.CharField(max_length=100)
    forum_last_post_time = models.IntegerField()
    forum_last_poster_name = models.CharField(max_length=255)
    forum_last_poster_colour = models.CharField(max_length=6)
    forum_flags = models.IntegerField()
    display_on_index = models.IntegerField()
    enable_indexing = models.IntegerField()
    enable_icons = models.IntegerField()
    enable_prune = models.IntegerField()
    prune_next = models.IntegerField()
    prune_days = models.IntegerField()
    prune_viewed = models.IntegerField()
    prune_freq = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_forums'


class Phpbb3ForumsAccess(models.Model):
    forum_id = models.IntegerField()
    user_id = models.IntegerField()
    session_id = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'phpbb3_forums_access'


class Phpbb3ForumsTrack(models.Model):
    user_id = models.IntegerField()
    forum_id = models.IntegerField()
    mark_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_forums_track'


class Phpbb3ForumsWatch(models.Model):
    forum_id = models.IntegerField()
    user_id = models.IntegerField()
    notify_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_forums_watch'


class Phpbb3GamesList(models.Model):
    game_id = models.IntegerField(primary_key=True)
    game_title = models.CharField(max_length=100)
    game_image = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'phpbb3_games_list'


class Phpbb3GamesPlayed(models.Model):
    record = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    game_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_games_played'


class Phpbb3Groups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_type = models.IntegerField()
    group_founder_manage = models.IntegerField()
    group_name = models.CharField(max_length=255)
    group_desc = models.TextField()
    group_desc_bitfield = models.CharField(max_length=255)
    group_desc_options = models.IntegerField()
    group_desc_uid = models.CharField(max_length=8)
    group_display = models.IntegerField()
    group_avatar = models.CharField(max_length=255)
    group_avatar_type = models.IntegerField()
    group_avatar_width = models.IntegerField()
    group_avatar_height = models.IntegerField()
    group_rank = models.IntegerField()
    group_colour = models.CharField(max_length=6)
    group_sig_chars = models.IntegerField()
    group_receive_pm = models.IntegerField()
    group_message_limit = models.IntegerField()
    group_legend = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_groups'


class Phpbb3Icons(models.Model):
    icons_id = models.IntegerField(primary_key=True)
    icons_url = models.CharField(max_length=255)
    icons_width = models.IntegerField()
    icons_height = models.IntegerField()
    icons_order = models.IntegerField()
    display_on_posting = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_icons'


class Phpbb3Lang(models.Model):
    lang_id = models.IntegerField(primary_key=True)
    lang_iso = models.CharField(max_length=30)
    lang_dir = models.CharField(max_length=30)
    lang_english_name = models.CharField(max_length=100)
    lang_local_name = models.CharField(max_length=255)
    lang_author = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'phpbb3_lang'


class Phpbb3Log(models.Model):
    log_id = models.IntegerField(primary_key=True)
    log_type = models.IntegerField()
    user_id = models.IntegerField()
    forum_id = models.IntegerField()
    topic_id = models.IntegerField()
    reportee_id = models.IntegerField()
    log_ip = models.CharField(max_length=40)
    log_time = models.IntegerField()
    log_operation = models.TextField()
    log_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'phpbb3_log'


class Phpbb3Medals(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    dynamic = models.IntegerField()
    device = models.CharField(max_length=32)
    number = models.IntegerField()
    parent = models.IntegerField()
    nominated = models.IntegerField()
    order_id = models.IntegerField()
    description = models.CharField(max_length=256, blank=True)
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_medals'


class Phpbb3MedalsAwarded(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    medal_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    awarder_id = models.BigIntegerField()
    awarder_un = models.CharField(max_length=255)
    awarder_color = models.CharField(max_length=6)
    time = models.IntegerField()
    nominated = models.IntegerField()
    nominated_reason = models.TextField()
    points = models.IntegerField()
    bbuid = models.CharField(max_length=255)
    bitfield = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'phpbb3_medals_awarded'


class Phpbb3MedalsCats(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=30)
    order_id = models.IntegerField()
    game_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_medals_cats'


class Phpbb3ModeratorCache(models.Model):
    forum_id = models.IntegerField()
    user_id = models.IntegerField()
    username = models.CharField(max_length=255)
    group_id = models.IntegerField()
    group_name = models.CharField(max_length=255)
    display_on_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_moderator_cache'


class Phpbb3Modules(models.Model):
    module_id = models.IntegerField(primary_key=True)
    module_enabled = models.IntegerField()
    module_display = models.IntegerField()
    module_basename = models.CharField(max_length=255)
    module_class = models.CharField(max_length=10)
    parent_id = models.IntegerField()
    left_id = models.IntegerField()
    right_id = models.IntegerField()
    module_langname = models.CharField(max_length=255)
    module_mode = models.CharField(max_length=255)
    module_auth = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'phpbb3_modules'


class Phpbb3PollOptions(models.Model):
    poll_option_id = models.IntegerField()
    topic_id = models.IntegerField()
    poll_option_text = models.TextField()
    poll_option_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_poll_options'


class Phpbb3PollVotes(models.Model):
    topic_id = models.IntegerField()
    poll_option_id = models.IntegerField()
    vote_user_id = models.IntegerField()
    vote_user_ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'phpbb3_poll_votes'


class Phpbb3Posts(models.Model):
    post_id = models.IntegerField(primary_key=True)
    topic_id = models.IntegerField()
    forum_id = models.IntegerField()
    poster_id = models.IntegerField()
    icon_id = models.IntegerField()
    poster_ip = models.CharField(max_length=40)
    post_time = models.IntegerField()
    post_approved = models.IntegerField()
    post_reported = models.IntegerField()
    enable_bbcode = models.IntegerField()
    enable_smilies = models.IntegerField()
    enable_magic_url = models.IntegerField()
    enable_sig = models.IntegerField()
    post_username = models.CharField(max_length=255)
    post_subject = models.CharField(max_length=100)
    post_text = models.TextField()
    post_checksum = models.CharField(max_length=32)
    post_attachment = models.IntegerField()
    bbcode_bitfield = models.CharField(max_length=255)
    bbcode_uid = models.CharField(max_length=8)
    post_postcount = models.IntegerField()
    post_edit_time = models.IntegerField()
    post_edit_reason = models.CharField(max_length=255)
    post_edit_user = models.IntegerField()
    post_edit_count = models.IntegerField()
    post_edit_locked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_posts'


class Phpbb3Privmsgs(models.Model):
    msg_id = models.IntegerField(primary_key=True)
    root_level = models.IntegerField()
    author_id = models.IntegerField()
    icon_id = models.IntegerField()
    author_ip = models.CharField(max_length=40)
    message_time = models.IntegerField()
    enable_bbcode = models.IntegerField()
    enable_smilies = models.IntegerField()
    enable_magic_url = models.IntegerField()
    enable_sig = models.IntegerField()
    message_subject = models.CharField(max_length=100)
    message_text = models.TextField()
    message_edit_reason = models.CharField(max_length=255)
    message_edit_user = models.IntegerField()
    message_attachment = models.IntegerField()
    bbcode_bitfield = models.CharField(max_length=255)
    bbcode_uid = models.CharField(max_length=8)
    message_edit_time = models.IntegerField()
    message_edit_count = models.IntegerField()
    to_address = models.TextField()
    bcc_address = models.TextField()

    class Meta:
        managed = False
        db_table = 'phpbb3_privmsgs'


class Phpbb3PrivmsgsFolder(models.Model):
    folder_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    folder_name = models.CharField(max_length=255)
    pm_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_privmsgs_folder'


class Phpbb3PrivmsgsRules(models.Model):
    rule_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    rule_check = models.IntegerField()
    rule_connection = models.IntegerField()
    rule_string = models.CharField(max_length=255)
    rule_user_id = models.IntegerField()
    rule_group_id = models.IntegerField()
    rule_action = models.IntegerField()
    rule_folder_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_privmsgs_rules'


class Phpbb3PrivmsgsTo(models.Model):
    msg_id = models.IntegerField()
    user_id = models.IntegerField()
    author_id = models.IntegerField()
    pm_deleted = models.IntegerField()
    pm_new = models.IntegerField()
    pm_unread = models.IntegerField()
    pm_replied = models.IntegerField()
    pm_marked = models.IntegerField()
    pm_forwarded = models.IntegerField()
    folder_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_privmsgs_to'


class Phpbb3ProfileFields(models.Model):
    field_id = models.IntegerField(primary_key=True)
    field_name = models.CharField(max_length=255)
    field_type = models.IntegerField()
    field_ident = models.CharField(max_length=20)
    field_length = models.CharField(max_length=20)
    field_minlen = models.CharField(max_length=255)
    field_maxlen = models.CharField(max_length=255)
    field_novalue = models.CharField(max_length=255)
    field_default_value = models.CharField(max_length=255)
    field_validation = models.CharField(max_length=20)
    field_required = models.IntegerField()
    field_show_on_reg = models.IntegerField()
    field_hide = models.IntegerField()
    field_no_view = models.IntegerField()
    field_active = models.IntegerField()
    field_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_profile_fields'


class Phpbb3ProfileFieldsData(models.Model):
    user_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'phpbb3_profile_fields_data'


class Phpbb3ProfileFieldsLang(models.Model):
    field_id = models.IntegerField()
    lang_id = models.IntegerField()
    option_id = models.IntegerField()
    field_type = models.IntegerField()
    lang_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'phpbb3_profile_fields_lang'


class Phpbb3ProfileLang(models.Model):
    field_id = models.IntegerField()
    lang_id = models.IntegerField()
    lang_name = models.CharField(max_length=255)
    lang_explain = models.TextField()
    lang_default_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'phpbb3_profile_lang'


class Phpbb3Ranks(models.Model):
    rank_id = models.IntegerField(primary_key=True)
    rank_title = models.CharField(max_length=255)
    rank_min = models.IntegerField()
    rank_special = models.IntegerField()
    rank_image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'phpbb3_ranks'


class Phpbb3Reports(models.Model):
    report_id = models.IntegerField(primary_key=True)
    reason_id = models.IntegerField()
    post_id = models.IntegerField()
    user_id = models.IntegerField()
    user_notify = models.IntegerField()
    report_closed = models.IntegerField()
    report_time = models.IntegerField()
    report_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'phpbb3_reports'


class Phpbb3ReportsReasons(models.Model):
    reason_id = models.IntegerField(primary_key=True)
    reason_title = models.CharField(max_length=255)
    reason_description = models.TextField()
    reason_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_reports_reasons'


class Phpbb3SearchResults(models.Model):
    search_key = models.CharField(primary_key=True, max_length=32)
    search_time = models.IntegerField()
    search_keywords = models.TextField()
    search_authors = models.TextField()

    class Meta:
        managed = False
        db_table = 'phpbb3_search_results'


class Phpbb3SearchWordlist(models.Model):
    word_id = models.IntegerField(primary_key=True)
    word_text = models.CharField(unique=True, max_length=255)
    word_common = models.IntegerField()
    word_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_search_wordlist'


class Phpbb3SearchWordmatch(models.Model):
    post_id = models.IntegerField()
    word_id = models.IntegerField()
    title_match = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_search_wordmatch'


class Phpbb3Sessions(models.Model):
    session_id = models.CharField(primary_key=True, max_length=32)
    session_user_id = models.IntegerField()
    session_last_visit = models.IntegerField()
    session_start = models.IntegerField()
    session_time = models.IntegerField()
    session_ip = models.CharField(max_length=40)
    session_browser = models.CharField(max_length=150)
    session_forwarded_for = models.CharField(max_length=255)
    session_page = models.CharField(max_length=255)
    session_viewonline = models.IntegerField()
    session_autologin = models.IntegerField()
    session_admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_sessions'


class Phpbb3SessionsKeys(models.Model):
    key_id = models.CharField(max_length=32)
    user_id = models.IntegerField()
    last_ip = models.CharField(max_length=40)
    last_login = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_sessions_keys'


class Phpbb3Sitelist(models.Model):
    site_id = models.IntegerField(primary_key=True)
    site_ip = models.CharField(max_length=40)
    site_hostname = models.CharField(max_length=255)
    ip_exclude = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_sitelist'


class Phpbb3Smilies(models.Model):
    smiley_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=50)
    emotion = models.CharField(max_length=50)
    smiley_url = models.CharField(max_length=50)
    smiley_width = models.IntegerField()
    smiley_height = models.IntegerField()
    smiley_order = models.IntegerField()
    display_on_posting = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_smilies'


class Phpbb3Styles(models.Model):
    style_id = models.IntegerField(primary_key=True)
    style_name = models.CharField(unique=True, max_length=255)
    style_copyright = models.CharField(max_length=255)
    style_active = models.IntegerField()
    template_id = models.IntegerField()
    theme_id = models.IntegerField()
    imageset_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_styles'


class Phpbb3StylesImageset(models.Model):
    imageset_id = models.IntegerField(primary_key=True)
    imageset_name = models.CharField(unique=True, max_length=255)
    imageset_copyright = models.CharField(max_length=255)
    imageset_path = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'phpbb3_styles_imageset'


class Phpbb3StylesImagesetData(models.Model):
    image_id = models.IntegerField(primary_key=True)
    image_name = models.CharField(max_length=200)
    image_filename = models.CharField(max_length=200)
    image_lang = models.CharField(max_length=30)
    image_height = models.IntegerField()
    image_width = models.IntegerField()
    imageset_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_styles_imageset_data'


class Phpbb3StylesTemplate(models.Model):
    template_id = models.IntegerField(primary_key=True)
    template_name = models.CharField(unique=True, max_length=255)
    template_copyright = models.CharField(max_length=255)
    template_path = models.CharField(max_length=100)
    bbcode_bitfield = models.CharField(max_length=255)
    template_storedb = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_styles_template'


class Phpbb3StylesTemplateData(models.Model):
    template_id = models.IntegerField()
    template_filename = models.CharField(max_length=100)
    template_included = models.TextField()
    template_mtime = models.IntegerField()
    template_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'phpbb3_styles_template_data'


class Phpbb3StylesTheme(models.Model):
    theme_id = models.IntegerField(primary_key=True)
    theme_name = models.CharField(unique=True, max_length=255)
    theme_copyright = models.CharField(max_length=255)
    theme_path = models.CharField(max_length=100)
    theme_storedb = models.IntegerField()
    theme_mtime = models.IntegerField()
    theme_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'phpbb3_styles_theme'


class Phpbb3Topics(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    forum_id = models.IntegerField()
    icon_id = models.IntegerField()
    topic_attachment = models.IntegerField()
    topic_approved = models.IntegerField()
    topic_reported = models.IntegerField()
    topic_title = models.CharField(max_length=100)
    topic_poster = models.IntegerField()
    topic_time = models.IntegerField()
    topic_time_limit = models.IntegerField()
    topic_views = models.IntegerField()
    topic_replies = models.IntegerField()
    topic_replies_real = models.IntegerField()
    topic_status = models.IntegerField()
    topic_type = models.IntegerField()
    topic_first_post_id = models.IntegerField()
    topic_first_poster_name = models.CharField(max_length=255)
    topic_first_poster_colour = models.CharField(max_length=6)
    topic_last_post_id = models.IntegerField()
    topic_last_poster_id = models.IntegerField()
    topic_last_poster_name = models.CharField(max_length=255)
    topic_last_poster_colour = models.CharField(max_length=6)
    topic_last_post_subject = models.CharField(max_length=100)
    topic_last_post_time = models.IntegerField()
    topic_last_view_time = models.IntegerField()
    topic_moved_id = models.IntegerField()
    topic_bumped = models.IntegerField()
    topic_bumper = models.IntegerField()
    poll_title = models.CharField(max_length=255)
    poll_start = models.IntegerField()
    poll_length = models.IntegerField()
    poll_max_options = models.IntegerField()
    poll_last_vote = models.IntegerField()
    poll_vote_change = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_topics'


class Phpbb3TopicsPosted(models.Model):
    user_id = models.IntegerField()
    topic_id = models.IntegerField()
    topic_posted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_topics_posted'


class Phpbb3TopicsTrack(models.Model):
    user_id = models.IntegerField()
    topic_id = models.IntegerField()
    forum_id = models.IntegerField()
    mark_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_topics_track'


class Phpbb3TopicsViews(models.Model):
    topic_id = models.IntegerField()
    user_id = models.IntegerField()
    view_count = models.IntegerField()
    last_view_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_topics_views'


class Phpbb3TopicsWatch(models.Model):
    topic_id = models.IntegerField()
    user_id = models.IntegerField()
    notify_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_topics_watch'


class Phpbb3UserGroup(models.Model):
    group_id = models.IntegerField()
    user_id = models.IntegerField()
    group_leader = models.IntegerField()
    user_pending = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_user_group'


class Phpbb3Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_type = models.IntegerField()
    group_id = models.IntegerField()
    user_permissions = models.TextField()
    user_perm_from = models.IntegerField()
    user_ip = models.CharField(max_length=40)
    user_regdate = models.IntegerField()
    username = models.CharField(max_length=255)
    username_clean = models.CharField(unique=True, max_length=255)
    user_password = models.CharField(max_length=40)
    user_passchg = models.IntegerField()
    user_pass_convert = models.IntegerField()
    user_email = models.CharField(max_length=100)
    user_email_hash = models.BigIntegerField()
    user_birthday = models.CharField(max_length=10)
    user_lastvisit = models.IntegerField()
    user_lastmark = models.IntegerField()
    user_lastpost_time = models.IntegerField()
    user_lastpage = models.CharField(max_length=200)
    user_last_confirm_key = models.CharField(max_length=10)
    user_last_search = models.IntegerField()
    user_warnings = models.IntegerField()
    user_last_warning = models.IntegerField()
    user_login_attempts = models.IntegerField()
    user_inactive_reason = models.IntegerField()
    user_inactive_time = models.IntegerField()
    user_posts = models.IntegerField()
    user_lang = models.CharField(max_length=30)
    user_timezone = models.DecimalField(max_digits=5, decimal_places=2)
    user_dst = models.IntegerField()
    user_dateformat = models.CharField(max_length=30)
    user_style = models.IntegerField()
    user_rank = models.IntegerField()
    user_colour = models.CharField(max_length=6)
    user_new_privmsg = models.IntegerField()
    user_unread_privmsg = models.IntegerField()
    user_last_privmsg = models.IntegerField()
    user_message_rules = models.IntegerField()
    user_full_folder = models.IntegerField()
    user_emailtime = models.IntegerField()
    user_topic_show_days = models.IntegerField()
    user_topic_sortby_type = models.CharField(max_length=1)
    user_topic_sortby_dir = models.CharField(max_length=1)
    user_post_show_days = models.IntegerField()
    user_post_sortby_type = models.CharField(max_length=1)
    user_post_sortby_dir = models.CharField(max_length=1)
    user_notify = models.IntegerField()
    user_notify_pm = models.IntegerField()
    user_notify_type = models.IntegerField()
    user_allow_pm = models.IntegerField()
    user_allow_viewonline = models.IntegerField()
    user_allow_viewemail = models.IntegerField()
    user_allow_massemail = models.IntegerField()
    user_options = models.IntegerField()
    user_avatar = models.CharField(max_length=255)
    user_avatar_type = models.IntegerField()
    user_avatar_width = models.IntegerField()
    user_avatar_height = models.IntegerField()
    user_sig = models.TextField()
    user_sig_bbcode_uid = models.CharField(max_length=8)
    user_sig_bbcode_bitfield = models.CharField(max_length=255)
    user_from = models.CharField(max_length=100)
    user_icq = models.CharField(max_length=15)
    user_aim = models.CharField(max_length=255)
    user_yim = models.CharField(max_length=255)
    user_msnm = models.CharField(max_length=255)
    user_jabber = models.CharField(max_length=255)
    user_website = models.CharField(max_length=200)
    user_occ = models.TextField()
    user_interests = models.TextField()
    user_actkey = models.CharField(max_length=32)
    user_newpasswd = models.CharField(max_length=40)
    user_form_salt = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'phpbb3_users'


class Phpbb3Warnings(models.Model):
    warning_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    log_id = models.IntegerField()
    warning_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_warnings'


class Phpbb3Words(models.Model):
    word_id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=255)
    replacement = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'phpbb3_words'


class Phpbb3Wwh(models.Model):
    rolling = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=15)
    id = models.IntegerField()
    viewonline = models.IntegerField()
    last_page = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_wwh'


class Phpbb3Zebra(models.Model):
    user_id = models.IntegerField()
    zebra_id = models.IntegerField()
    friend = models.IntegerField()
    foe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'phpbb3_zebra'
