# Maintainer: Antonio Medeiros <linuxkamarada@gmail.com>

pkgname=kamarada-gnome-backgrounds
pkgver=20250904
pkgrel=1
pkgdesc='Background images and data for Linux Kamarada GNOME'
arch=(any)
url='https://github.com/kamarada/branding'
license=('GPL-3.0')
makedepends=('git')
optdepends=('manjaro-gnome-backgrounds')
source=('git+https://github.com/kamarada/branding.git#branch=testing')
sha256sums=('SKIP')

prepare() {
    cd "$srcdir/branding"

    cd "wallpaper"
    rm -rf backgrounds/kamarada/original/
    rm -rf wallpapers/*/original
}

package() {
    set -ex
    echo "Installing files for $pkgname"

    cd "$srcdir/branding"

    # wallpaper
    cd "wallpaper"
    mkdir -p "$pkgdir/usr/share/backgrounds"
    mv backgrounds/* "$pkgdir/usr/share/backgrounds/"
    mkdir -p "$pkgdir/usr/share/gnome-background-properties"
    mv gnome-background-properties/* "$pkgdir/usr/share/gnome-background-properties/"
    mkdir -p "$pkgdir/usr/share/wallpapers"
    mv wallpapers/* "$pkgdir/usr/share/wallpapers/"
}
