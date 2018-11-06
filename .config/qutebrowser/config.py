import subprocess
config.load_autoconfig()

# X configs change options / QB features
config.bind('xc', 'config-cycle tabs.show always never')
config.bind('xx', 'set tabs.show always;; later 5000 set tabs.show switching')
config.bind('xg', 'tab-give')
config.bind('zd', 'download-open')
config.bind('xb', 'config-cycle statusbar.hide')
config.bind('xh', 'config-cycle content.user_stylesheets /home/gazbit/.config/qutebrowser/styles/solarized-dark-all-sites.css ""')
config.bind('B', 'set-cmd-text -s :bookmark-load')
config.bind('xs', 'config-source')

# Z configs are for downloading videos and music
config.bind('zy', 'hint links spawn ~/bin/ytdv {hint-url} ~/Downloads/qbdownloads')
config.bind('zp', 'hint links spawn ~/bin/ytdlp {hint-url} ~/Downloads/qbdownloads')
config.bind('zv', 'spawn ~/bin/ytdv {url} ~/Downloads/qbdownloads')

# Ctrl shortcuts run scripts / applications
config.bind('<Ctrl-m>', 'spawn --detach mpv --force-window yes {url}')
config.bind('<Ctrl-Shift-p>', 'spawn --userscript password_fill')
config.bind('<Ctrl-r>', 'spawn --userscript readability')
config.bind('<Ctrl-y>', 'hint links spawn --detach mpv --force-window yes {hint-url}')

# This one is a special one that opens all my pinned tabs
config.bind('xo','open https://mail.protonmail.com/login;;tab-pin;;open -t https://www.youtube.com/dashboard?o=U;;tab-pin;;open -t https://hackmd.io/recent#;;tab-pin;;open -t https://linuxrocks.online/web/timelines/public/local;;tab-pin;;open -t https://cloud.xpenguin.club;;tab-pin')

# Unbind shite defaults
config.unbind('q')
config.unbind('z')
config.unbind('<Ctrl-v>')


# c.? are options set at launch.
c.tabs.favicons.scale = 1
c.tabs.indicator.padding = {"top": 0, "right": 0, "bottom": 0, "left": 0}
c.tabs.position = "left"
c.tabs.show = "switching"
c.tabs.title.format = ""
c.tabs.width = 36
c.content.cookies.accept = 'all'
c.content.geolocation = 'ask'
c.content.webgl = True
c.downloads.remove_finished = 800
c.auto_save.session = True
c.editor.command = ["termite", "-e", "nvim '{}'"]

# search engine shortneners
c.url.searchengines = {
"DEFAULT": "https://duckduckgo.com/?q={}",
"goog": "https://www.google.co.uk/search?&q={}",
"googi": "https://www.google.co.uk/search?q={}&tbm=isch",
"wiki": "https://en.wikipedia.org/w/index.php?search={}",
"steam": "http://store.steampowered.com/search/?term={}",
"ddg": "https://duckduckgo.com/?q={}",
"aur": "https://aur.archlinux.org/packages/?O=0&K={}",
"arch": "https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}",
"imdb": "http://www.imdb.com/find?ref_=nv_sr_fn&s=all&q={}",
"dic": "http://www.dictionary.com/browse/{}",
"ety": "http://www.etymonline.com/index.php?allowed_in_frame=0&search={}",
"urban": "http://www.urbandictionary.com/define.php?term={}",
"yt": "https://www.youtube.com/results?search_query={}",
"ddgi": "https://duckduckgo.com/?q={}&iar=images",
"lutris": "https://lutris.net/games/?q={}",
"deal":"https://isthereanydeal.com/search/?q={}",
"gog":"https://www.gog.com/games?sort=popularity&search={}&page=1",
"proton":"https://www.protondb.com/search?q={}",
"itch": "https://itch.io/search?q={}"}

# call my folder shortcuts scripts
config.source('shortcuts.py')
