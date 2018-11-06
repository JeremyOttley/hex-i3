#!/usr/bin/env ruby

apps = %w[
  feh
  i3-gaps-next-git
  zsh
  mpv-full-git
  compton-git
  redshift-git
  redshift-gtk-git
  i3status-git
  dunst
  youtube-dl-git
  youtube-mpv-git
  qutebrowser-git
  cava
  spotify
  i3blocks-git
  rofi-git
  i3lock-color
  j4-dmenu-desktop
  pavucontrol-qt-git
  rvm
  git
  emacs
  neovim-git
  xfce4-taskmanager-git
  caffeine-ng
  lutris-git
  deluge-git
  visual-studio-code-bin
  streamlink-twitch-gui
  nautilus
  filemanager-actions 
  nautilus-terminal 
  nautilus-sendto 
  file-roller
  kitty-git
]

install = ->app{ `trizen -Syu --noconfirm #{app}` }

## GRABS
def grab_wallpaper
status = system("git clone https://github.com/jeremyottley/.wallpapers ~/.wallpapers")
puts status ? "Success" : "Failed"
end

def grab_fonts
status = system("git clone https://github.com/jeremyottley/.fonts ~/.fonts")
puts status ? "Success" : "Failed"
`fc-cache -fv`
end

## MAIN ##
grab_wallpaper
grab_fonts
Dir.glob("#{Dir.home}/hex-i3/.", File::FNM_DOTMATCH).each { |f| FileUtils.cp_r("#{f}", DESTINATION, :verbose => true) }

apps.each &install
