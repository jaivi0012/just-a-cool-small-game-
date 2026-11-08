#!/bin/bash
set -e
[ -d venv ] || python3 -m venv venv
source venv/bin/activate
pip install pygame pyinstaller

rm -rf build dist *.spec _assets SurvivalGame.AppDir
mkdir _assets
for d in SoldierWalk Sounds tntExplode OrcWalk Boss backgroundImg; do
    [ -d "$d" ] && cp -r "$d" _assets/
done
for f in *.png *.jpeg *.jpg; do
    [ -f "$f" ] && cp "$f" _assets/
done

pyinstaller --onefile --add-data "_assets:." --paths . --hidden-import newLoad game.py

mkdir -p SurvivalGame.AppDir/usr/bin
cp dist/game SurvivalGame.AppDir/usr/bin/game
cp Orc1.png SurvivalGame.AppDir/survivalgame.png

cat > SurvivalGame.AppDir/survivalgame.desktop <<'EOF'
[Desktop Entry]
Type=Application
Name=Survival Game
Exec=game
Icon=survivalgame
Categories=Game;
EOF

cat > SurvivalGame.AppDir/AppRun <<'EOF'
#!/bin/sh
HERE="$(dirname "$(readlink -f "$0")")"
exec "$HERE/usr/bin/game" "$@"
EOF
chmod +x SurvivalGame.AppDir/AppRun

[ -f appimagetool-x86_64.AppImage ] || {
    wget https://github.com/AppImage/appimagetool/releases/download/continuous/appimagetool-x86_64.AppImage
    chmod +x appimagetool-x86_64.AppImage
}
ARCH=x86_64 ./appimagetool-x86_64.AppImage --appimage-extract-and-run SurvivalGame.AppDir SurvivalGame-x86_64.AppImage
ls -lh SurvivalGame-x86_64.AppImage
