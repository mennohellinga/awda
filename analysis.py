#!/usr/bin/python3

###############################################################################
# GE3V17043 --- Soldiers, Guerrillas, Terrorists
# Data analysis for the Atomwaffen posts in the leaked Iron March database
# M. Hellinga, 12 Nov. 2019 - ENDDATE
#
# This program will:
#   --- describe the tables relevant to researching the AWD organisational
#       structure
#   --- create a list of users who post on the AWD
#   --- export its results in LaTeX
#
# INPUT:
#   The directory from which the program is called, must contain a subdirectory
#   called data, which must contain the following files, all of which are
#   output by the scripts, contained in the torrent, which convert the original
#   database to sqlite3.
#       --- core_members.db
#       --- core_message_posts.db
#       --- core_message_topics.db
#       --- core_search_index.db
#
# OUTPUT:
#   The program will make a directory called LaTeX in its working directory.
#   If it already exists, all data will be cleared from it. The following
#   files will be created:
#       --- master.tex: the coordinating, master document. This file brings all
#               the others together.
#       --- core_members_description.tex: describes the table containing all
#               known Iron March members at the time of the snapshot.
#       --- core_message_posts.tex: describes the table containing all known
#               private messages on Iron March
#       --- core_message_topics.tex: describes the table containing all known
#               thread topics on Iron March
#       --- core_search_index.tex: describes the table containing all known
#               forum posts on Iron March.
#       --- awd_posters.tex: a table of all users who posted about the AWD
#
# OPERATING SYSTEM:
#   This program has only been tested on a Linux system.
#
# CAVEATS:
#   This program will not work if it does not have rwx access to its working
#   directory and all its subdirectories.
#
#   This program will not work if the specified input files are absent.
#
#   This program might not fail gracefully.
###############################################################################

import datetime
import sqlite3

import lt
import lt_strings

lt.master_open()

def describetable_lt(connection, name):
    '''
        describetable_lt(connection, name)

        Retrieves a list of columns from table <name>, in the database connected
        to <connection>. Prints a table containing each column's ID, name and
        type in a LaTeX tabular environment at lt_path+<name>+'.tex'
    '''

    table = []

    # this looks hideously insecure. Which it would be, if this function were
    # not guaranteed to receive safe and sane arguments

    c = connection.cursor()
    for t in c.execute('''pragma table_info('''+name+''')'''):
        table = table + [[repr(t[0]),lt.safe(t[1]),lt.safe(t[2])]]

    lt.print_table(name, lt.safe(name)+" — Table Description", r'''Created with describetable\_lt(\emph{<connection>}, '''+lt.safe(name)+")", "cll", ["ID", "name", "type"], table)

conn = sqlite3.connect('data/core_members.db')
describetable_lt(conn, 'core_members')

conn = sqlite3.connect('data/core_message_posts.db')
describetable_lt(conn, 'core_message_posts')

conn = sqlite3.connect('data/core_message_topics.db')
describetable_lt(conn, 'core_message_topics')

conn = sqlite3.connect('data/core_search_index.db')
describetable_lt(conn, 'core_search_index')

#
# Now, having described the main tables, we will compile a list of users who
# have posted on the AWD.
#

awd_users_heading = [r'''member\_id''', "name", "joined", r'''\awd\ posts''', "total posts", r'''\% \awd\ posts''']
awd_users = []

searchindex = sqlite3.connect("data/core_search_index.db").cursor()
for ID in searchindex.execute(  '''
                                    SELECT DISTINCT index_author
                                    FROM core_search_index
                                    WHERE index_content LIKE '%atomwaffen%'
                                    COLLATE NOCASE
                                    ORDER BY index_author
                                '''):
    awd_users = awd_users + [[repr(ID[0])]]

# index_author 0 is matched to a number of posts, but does not occur in core_members
awd_users = awd_users[1:]

tmp = []
coremembers = sqlite3.connect("data/core_members.db").cursor()
for user in awd_users:
    member = coremembers.execute(   '''
                                        SELECT name, joined, member_posts
                                        FROM core_members
                                        WHERE member_id = '''+ user[0] + '''
                                    ''').fetchall()
    name = member[0][0]
    joined = member[0][1]
    member_posts = member[0][2]

    awd_posts = searchindex.execute(    '''
                                            SELECT COUNT(*)
                                            FROM core_search_index
                                            WHERE index_author = ''' + user[0] + '''
                                            AND index_content LIKE "%atomwaffen%"
                                            COLLATE NOCASE
                                        ''').fetchall()[0][0]
    tmp = tmp + [[user[0], name, joined, awd_posts, member_posts, awd_posts/member_posts]]

awd_users = tmp

awd_users_printable = []
for user in awd_users:
    user[1] = lt.safe(user[1])
    user[2] = datetime.datetime.utcfromtimestamp(user[2]).strftime('%Y/%m/%d')

    user[3] = repr(user[3])
    user[4] = repr(user[4])
    user[5] = lt.safe('{:.2%}'.format(user[5]))

    awd_users_printable = awd_users_printable + [user]

lt.print_table("awd_users", 'Users who posted about the AWD', "", "cllccc", awd_users_heading, awd_users_printable)

lt.master_close()
