var panel = new Panel
var panelScreen = panel.screen
var freeEdges = {"bottom": true, "top": true, "left": true, "right": true}

for (i = 0; i < panelIds.length; ++i) {
    var tmpPanel = panelById(panelIds[i])
    if (tmpPanel.screen == panelScreen) {
        // Ignore the new panel
        if (tmpPanel.id != panel.id) {
            freeEdges[tmpPanel.location] = false;
        }
    }
}

if (freeEdges["bottom"] == true) {
    panel.location = "bottom";
} else if (freeEdges["top"] == true) {
    panel.location = "top";
} else if (freeEdges["left"] == true) {
    panel.location = "left";
} else if (freeEdges["right"] == true) {
    panel.location = "right";
} else {
    // There is no free edge, so leave the default value
    panel.location = "top";
}

// panel.height = screenGeometry(panel.screen).height > 899 ? 35 : 27
panel.height = 48
var launcher = panel.addWidget("launcher")
launcher.globalShortcut = "Alt+F1";
// panel.addWidget("org.kde.showActivityManager")
var pager = panel.addWidget("pager")
pager.writeConfig("hideWhenSingleDesktop", "true")
var tasks = panel.addWidget("icontasks")
var systemtray = panel.addWidget("systemtray")
var clock = panel.addWidget("digital-clock")
// show date besides time
clock.writeConfig("dateStyle", "3")
// avoid akonadi unless akonadi is started
clock.writeConfig("displayEvents", "false")
panel.addWidget("showdesktop")

tasks.currentConfigGroup = new Array("Launchers")
// tasks.writeConfig("browser", "preferred://browser, , , ")
// tasks.writeConfig("filemanager", "preferred://filemanager, , , ")
tasks.writeConfig("Items", "file:///usr/share/applications/firefox.desktop?wmClass=Firefox,file:///usr/share/applications/kde4/dolphin.desktop,file:///usr/share/applications/kde4/amarok.desktop?wmClass=Amarok,file:///usr/share/applications/vlc.desktop?wmClass=Vlc,file:///usr/share/applications/kde4/kwrite.desktop?wmClass=Kwrite,file:///usr/share/applications/kde4/kcalc.desktop?wmClass=Kcalc")