# awda
Course project for GE3V17043: Soldiers, Guerrillas, Terrorists. Queries the November 2019 Iron March database, to extract information about the Atomwaffen Division.

## Introduction

Founded in 2015, the American neo-nazi terrorist group Atomwaffen Division (AWD) has defied analysis. Though they present themselves as white supremacists, they flirt with islamic extremism — an ideology to which white ethno-nationalists are traditionally opposed. Furthermore, the nature of AWD's relationship with James Mason — the author of the ethno-nationalist Siege manifesto — and the Order of the Nine Angles — an esoteric Hitlerist/Satanist organisation — remain unclear, as does its organisational structure. [SPIEGEL]

On November 6, 2019 a torrent was released, containing the entire SQL database of the right-wing extremist Iron March forum. It contains the forum's user data, direct messages, and posts, ranging from its founding in 2011 to its termination in 2017. [BELLINGCAT]

This project aims to extract information on AWD's organisational structure from the Iron March database.

## Getting the data and installing the program

This software has only been tested on x64 Linux. Use on other systems is not recommended.

1. Make sure you have the following software installed:

  * Python 3.8.0-1 or higher.
  * Sqlite 3.30.1-1 or higher.
  * TeXLive, a version from November 2019, or later.
  * Standard Unix tools such as sh and Make.
1. Clone the repository with `git clone https://github.com/mennohellinga/awda`
1. Download the dataset via [IRONMARCH]
1. Follow the instructions in `iron_march_201911/README` to generate a set of sqlite databases under `iron_march_201911/split_sqlite`
1. Create a subdirectory in the cloned repository and call it `data` Copy the following files from `iron_march_201911/split_sqlite` into `awda/data`
  * `core_members.db`
  * `core_message_posts.db`
  * `core_message_topics.db`
  * `core_search_index.db`
1. Navigate to the top level of the cloned repository and run `run_linux.sh`

## Output

The software will create `awda.pdf`, containing the following information:

2. Table Descriptions
    1. Description of `core_members`
    1. Description of `core_message_posts`
    1. Description of `core_message_topics`
    1. Description of `core_search_index`

## To do

### High priority

- [ ] separate data-gathering from table printing functionality
- [ ] define all fixed LaTeX strings in a separate file
- [ ] create LaTeX header for stand-alone use of individual files
- [ ] create LaTeX code to display threads
- [ ] create Python code to retrieve threads
- [ ] move OS interaction to the shell script

### Low priority

### Long term

### Completed

## References

* **BELLINGCAT:** _Massive White Supremacist Message Board Leak: How to Access and Interpret the Data_, November 6, 2019, [link.](https://www.bellingcat.com/resources/how-tos/2019/11/06/massive-white-supremacist-message-board-leak-how-to-access-and-interpret-the-data/)
* **IRONMARCH:** The data set can be downloaded via the following magnet link: <magnet:?xt=urn:btih:f745eb1b86eb55f638517654c015fcaaadc96919&dn=iron_march_201911&tr=http%3a%2f%2fbt1.archive.org%3a6969%2fannounce&tr=http%3a%2f%2fbt2.archive.org%3a6969%2fannounce&ws=http%3a%2f%2fia601401.us.archive.org%2f17%2fitems%2f&ws=https%3a%2f%2fia801401.us.archive.org%2f17%2fitems%2f>
* **SPIEGEL:** Epp, Alexander, Roman Höffner, et al. "Das Hass-Netzwerk: »Atomwaffen Division« nennt sich eine militante Nazi-Gruppe in den USA. Wer steckt dahinter?" _Der Spiegel 71,_ 35, [link.](https://www.spiegel.de/politik/ausland/neonazi-zelle-atomwaffen-division-das-hass-netzwerk-a-1225341.html)
