#!/usr/bin/env ruby

apps = %w[
  i3
  zsh
  mpv
  compton
  redshift
  i3status
  dunst
  youtube-dl
  qutebrowser
  cava
  spotify
  i3blocks
  rofi-git
  i3lock
]
# streamlink vscode xfce4-taskmanager ranger lutris notify-send deluge caffeine mate-power-manager nextcloud nautilus kitty

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
