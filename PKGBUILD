# Maintainer: Antonio Medeiros <linuxkamarada@gmail.com>

pkgname=(
    'kamarada-distribution-logos'
    'kamarada-gnome-backgrounds'
)
pkgbase=branding
pkgver=20251003
pkgrel=1
arch=(any)
url='https://github.com/kamarada/branding'
license=('GPL-3.0')
makedepends=('git')
source=('git+https://github.com/kamarada/branding.git#branch=testing')
sha256sums=('SKIP')

pkgver() {
    cd "$pkgbase"
    git show -s --format=%cd --date=format:%Y%m%d HEAD
}

package_kamarada-distribution-logos() {
    pkgdesc='Icons with Linux Kamarada distribution logos'

    cd "$pkgbase/distribution-logos"
    install -Dm644 logo_text_white.png -t "$pkgdir/usr/share/pixmaps/kamarada-logo-text-dark.png"
    install -Dm644 logo_text_white.svg -t "$pkgdir/usr/share/pixmaps/kamarada-logo-text-dark.svg"
}

package_kamarada-gnome-backgrounds() {
    pkgdesc='Linux Kamarada default wallpapers'
    optdepends=('manjaro-gnome-backgrounds')

    cd "$pkgbase/wallpaper"
    rm -rf backgrounds/kamarada/original/
    rm -rf wallpapers/*/original
    mkdir -p "$pkgdir/usr/share/backgrounds"
    mv backgrounds/* "$pkgdir/usr/share/backgrounds/"
    mkdir -p "$pkgdir/usr/share/gnome-background-properties"
    mv gnome-background-properties/* "$pkgdir/usr/share/gnome-background-properties/"
    mkdir -p "$pkgdir/usr/share/wallpapers"
    mv wallpapers/* "$pkgdir/usr/share/wallpapers/"
}
