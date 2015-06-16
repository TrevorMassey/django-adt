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


class Applications(models.Model):
    record = models.IntegerField(primary_key=True)
    userrecord = models.IntegerField(unique=True)
    aim = models.CharField(max_length=80)
    charname = models.CharField(max_length=40)
    race = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    level = models.IntegerField()
    cclass = models.IntegerField()
    clevel = models.IntegerField()
    name = models.CharField(max_length=80)
    bday = models.DateField()
    gender = models.IntegerField()
    location = models.CharField(max_length=160)
    skill = models.CharField(max_length=15)
    playtime = models.TextField()
    history = models.TextField()
    whyjoin = models.TextField()
    raid = models.CharField(max_length=15)
    gamer = models.CharField(max_length=40)
    appdate = models.IntegerField()
    guildexperience = models.TextField()
    repeatcontent = models.TextField()
    personality = models.TextField()
    leadership = models.TextField()
    expectation = models.TextField()
    leveling = models.TextField()
    status = models.IntegerField()
    game = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'applications'


class ApplicationsQuestions(models.Model):
    record = models.IntegerField(primary_key=True)
    game = models.IntegerField()
    q1 = models.TextField()
    q2 = models.TextField()
    q3 = models.TextField()
    q4 = models.TextField()
    q5 = models.TextField()
    q6 = models.TextField()

    class Meta:
        managed = False
        db_table = 'applications_questions'


class Banned(models.Model):
    record = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=25)
    date = models.IntegerField()
    reason = models.TextField()
    address = models.CharField(max_length=255)
    com = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banned'


class Bannedsoft(models.Model):
    record = models.IntegerField(primary_key=True)
    date = models.IntegerField()
    reason = models.TextField()
    address = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'bannedsoft'


class Bugreport(models.Model):
    reportnumber = models.IntegerField(primary_key=True)
    record = models.IntegerField()
    report = models.TextField()
    browser = models.CharField(max_length=150)
    submitted = models.IntegerField()
    reviewed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bugreport'


class Calendar(models.Model):
    record = models.IntegerField(primary_key=True)
    type = models.IntegerField()
    status = models.IntegerField()
    timestamp = models.IntegerField()
    duration = models.IntegerField()
    title = models.CharField(max_length=255)
    info = models.TextField()
    raidnum = models.CharField(max_length=5)
    refnum = models.IntegerField()
    game = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calendar'


class Characters(models.Model):
    char_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    type = models.IntegerField()
    name = models.CharField(max_length=100)
    race = models.IntegerField()
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    level = models.IntegerField()
    game = models.IntegerField()
    sync = models.IntegerField()
    sync_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'characters'


class Chatbox(models.Model):
    postnum = models.IntegerField(primary_key=True)
    record = models.IntegerField()
    username = models.CharField(max_length=15)
    message = models.TextField()
    date = models.IntegerField()
    game = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chatbox'


class Comments(models.Model):
    record = models.IntegerField(primary_key=True)
    section = models.IntegerField()
    reference = models.IntegerField()
    poster_id = models.IntegerField()
    comment = models.TextField()
    timestamp = models.IntegerField()
    officer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comments'


class Cookies(models.Model):
    record = models.IntegerField(primary_key=True)
    cookiekey = models.IntegerField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cookies'


class Division(models.Model):
    divid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    leader = models.IntegerField()
    formed = models.IntegerField()
    goal = models.TextField()

    class Meta:
        managed = False
        db_table = 'division'


class Favor(models.Model):
    record = models.IntegerField(primary_key=True)
    user = models.IntegerField()
    mod = models.IntegerField()
    from_field = models.IntegerField(db_column='from')  # Field renamed because it was a Python reserved word.
    timestamp = models.IntegerField()
    reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'favor'


class GamesList(models.Model):
    record = models.IntegerField(primary_key=True)
    game_name = models.CharField(max_length=250)
    game_icon = models.CharField(max_length=250)
    game_icon_med = models.CharField(max_length=250)
    game_acr = models.CharField(max_length=10)
    launch = models.IntegerField()
    close = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'games_list'


class GamesPlaying(models.Model):
    record = models.IntegerField(primary_key=True)
    userrecord = models.IntegerField()
    game = models.IntegerField()
    start = models.IntegerField()
    stop = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'games_playing'


class Groups(models.Model):
    username = models.CharField(max_length=15, blank=True)
    rank = models.IntegerField(blank=True, null=True)
    game_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'groups'


class Leaderapp(models.Model):
    appnum = models.IntegerField(primary_key=True)
    record = models.IntegerField()
    text = models.TextField()
    rank = models.IntegerField()
    divid = models.IntegerField()
    sqdid = models.IntegerField()
    date = models.IntegerField()
    status = models.CharField(max_length=100)
    closereason = models.TextField()

    class Meta:
        managed = False
        db_table = 'leaderapp'


class Msgb(models.Model):
    msg_id = models.IntegerField()
    user_id = models.IntegerField()
    author_id = models.IntegerField()
    pm_deleted = models.IntegerField()
    pm_sentdeleted = models.TextField()
    pm_unread = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'msgb'


class News(models.Model):
    record = models.IntegerField(primary_key=True)
    creator = models.IntegerField()
    title = models.CharField(max_length=100)
    news = models.TextField()
    date = models.IntegerField()
    access = models.IntegerField()
    cat = models.IntegerField()
    image = models.CharField(max_length=250)
    approved = models.IntegerField()
    game = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'news'


class NewsCats(models.Model):
    record = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'news_cats'


class Poll(models.Model):
    record = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    vote = models.IntegerField()
    voter_id = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'poll'


class Privmsg(models.Model):
    msg_id = models.IntegerField(primary_key=True)
    author_id = models.IntegerField()
    message_time = models.IntegerField()
    subject = models.CharField(max_length=100)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'privmsg'


class PrivmsgTo(models.Model):
    msg_id = models.IntegerField()
    user_id = models.IntegerField()
    author_id = models.IntegerField()
    pm_deleted = models.IntegerField()
    pm_sentdeleted = models.IntegerField()
    pm_unread = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'privmsg_to'


class PvpInvites(models.Model):
    record = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    teamid = models.IntegerField()
    ladderid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pvp_invites'


class PvpLadders(models.Model):
    record = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    max = models.IntegerField()
    info = models.TextField()

    class Meta:
        managed = False
        db_table = 'pvp_ladders'


class PvpMatches(models.Model):
    record = models.IntegerField(primary_key=True)
    chal_id = models.IntegerField()
    def_id = models.IntegerField()
    ladder_id = models.IntegerField()
    season_id = models.IntegerField()
    chal_date = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pvp_matches'


class PvpMatchesWins(models.Model):
    record = models.IntegerField(primary_key=True)
    season_id = models.IntegerField()
    ladder_id = models.IntegerField()
    winner_id = models.IntegerField()
    loser_id = models.IntegerField()
    timestamp = models.IntegerField()
    xp_win = models.IntegerField()
    xp_loss = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pvp_matches_wins'


class PvpSeasons(models.Model):
    record = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    startstamp = models.IntegerField()
    stopstamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pvp_seasons'


class PvpTeams(models.Model):
    record = models.IntegerField(primary_key=True)
    ladder_id = models.IntegerField()
    name = models.CharField(max_length=250)
    timestamp = models.IntegerField()
    info = models.TextField()

    class Meta:
        managed = False
        db_table = 'pvp_teams'


class PvpTeamsMembers(models.Model):
    record = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    teamid = models.IntegerField()
    timestamp = models.IntegerField()
    leader = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pvp_teams_members'


class Quotes(models.Model):
    record = models.IntegerField(primary_key=True)
    poster = models.IntegerField()
    title = models.CharField(max_length=80)
    quote = models.TextField()
    type = models.TextField()
    image = models.TextField()
    posted = models.IntegerField()
    cat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quotes'


class QuotesHypes(models.Model):
    record = models.IntegerField(primary_key=True)
    quote = models.IntegerField()
    user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quotes_hypes'


class RaidAttendance(models.Model):
    record = models.IntegerField(primary_key=True)
    raid = models.IntegerField()
    charid = models.IntegerField()
    userid = models.IntegerField()
    game = models.IntegerField()
    startstamp = models.IntegerField()
    stopstamp = models.IntegerField()
    type = models.IntegerField()
    unscheduled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raid_attendance'


class RaidBonusdkp(models.Model):
    record = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    game = models.IntegerField()
    dkp = models.IntegerField()
    reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'raid_bonusdkp'


class RaidBosses(models.Model):
    record = models.IntegerField(primary_key=True)
    dungeon = models.IntegerField()
    name = models.CharField(max_length=255)
    dkp = models.IntegerField()
    game = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raid_bosses'


class RaidBosskills(models.Model):
    record = models.IntegerField(primary_key=True)
    raid = models.IntegerField()
    boss = models.IntegerField()
    charid = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raid_bosskills'


class RaidDungeons(models.Model):
    record = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    dkphour = models.IntegerField()
    game = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raid_dungeons'


class RaidItemlist(models.Model):
    record = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    game = models.IntegerField()
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'raid_itemlist'


class RaidItems(models.Model):
    record = models.IntegerField(primary_key=True)
    boss = models.IntegerField()
    raid = models.IntegerField()
    item = models.IntegerField()
    dkp = models.IntegerField()
    charid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raid_items'


class RaidPerf(models.Model):
    record = models.IntegerField(primary_key=True)
    raid = models.IntegerField()
    dungeon = models.IntegerField()
    userid = models.IntegerField()
    timestamp = models.IntegerField()
    from_userid = models.IntegerField()
    reason = models.TextField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raid_perf'


class RaidRaids(models.Model):
    record = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    dungeon = models.IntegerField()
    dkphour = models.IntegerField()
    unscheduled = models.IntegerField()
    startstamp = models.IntegerField()
    stopstamp = models.IntegerField()
    game = models.IntegerField()
    status = models.IntegerField()
    leader = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'raid_raids'


class Resources(models.Model):
    record = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    type = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resources'


class ResourcesCats(models.Model):
    record = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    game = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'resources_cats'


class RoleMapping(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleId', blank=True, null=True)  # Field name made lowercase.
    gameid = models.IntegerField(db_column='gameId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role_mapping'


class Roles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parent = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True)
    rank = models.TextField(blank=True)
    oid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Screenshots(models.Model):
    record = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=35)
    views = models.IntegerField()
    comments = models.IntegerField()
    timestamp = models.IntegerField()
    type = models.CharField(max_length=3)
    category = models.IntegerField()
    poster = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'screenshots'


class ScreenshotsCats(models.Model):
    record = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250)
    type = models.TextField()
    image = models.TextField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'screenshots_cats'


class Squad(models.Model):
    sqdid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    leader = models.IntegerField()
    formed = models.IntegerField()
    divid = models.IntegerField()
    goal = models.TextField()

    class Meta:
        managed = False
        db_table = 'squad'


class Users(models.Model):
    record = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    rank = models.IntegerField()
    email = models.CharField(max_length=80)
    aim = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    bday = models.DateField()
    gender = models.IntegerField()
    location = models.CharField(max_length=160)
    timezone = models.CharField(max_length=10)
    regdate = models.IntegerField()
    news = models.IntegerField()
    adduser = models.IntegerField()
    edituser = models.IntegerField()
    deluser = models.IntegerField()
    promote = models.IntegerField()
    timestamp = models.IntegerField()
    ip = models.CharField(max_length=40)
    file = models.CharField(max_length=100)
    onweb = models.IntegerField()
    raid = models.IntegerField()
    onvent = models.IntegerField()
    onaim = models.IntegerField()
    modcb = models.IntegerField()
    welcome = models.IntegerField()
    bugreport = models.IntegerField()
    squad = models.IntegerField()
    squaddate = models.IntegerField()
    clearpass = models.CharField(max_length=45)
    primary_game = models.IntegerField()
    tsuid = models.TextField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersPass(models.Model):
    record = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    updated = models.IntegerField()
    oldmd5 = models.CharField(max_length=255)
    oldclear = models.CharField(max_length=255)
    vent = models.IntegerField()
    newclear = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users_pass'


class Variables(models.Model):
    varnum = models.IntegerField(primary_key=True)
    type = models.TextField()

    class Meta:
        managed = False
        db_table = 'variables'


class VariablesMessages(models.Model):
    record = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    text = models.TextField()
    date = models.IntegerField()
    game = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'variables_messages'
