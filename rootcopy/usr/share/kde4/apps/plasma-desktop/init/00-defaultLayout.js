function widgetExists(name)
{
    var widgets = knownWidgetTypes;
    for (i in widgets) {
        if (widgets[i] == name) {
            return true;
        }
    }

    return false;
}

var topLeftScreen = 0
var rect = screenGeometry(0)

// find our "top left" screen to put the folderview on it
for (var i = 1; i < screenCount; ++i) {
    var g = screenGeometry(i)

    if (g.x <= rect.x && g.top >= rect.top) {
        rect = g
        topLeftScreen = i
    }
}

// var hasFolderview = widgetExists("folderview");

loadTemplate("org.kde.plasma-desktop.defaultPanel")

for (var i = 0; i < screenCount; ++i) {
    var desktop;
    
    if (i == topLeftScreen) {
	desktop = new Activity("folderview")
    } else {
	desktop = new Activity("desktop")
    }
    
    desktop.name = i18n("Desktop")
    desktop.screen = i
    desktop.wallpaperPlugin = 'image'
    desktop.wallpaperMode = 'SingleImage'

    /* if (hasFolderview && i == topLeftScreen) {
       var folderview = desktop.addWidget("folderview")
       folderview.writeConfig("url", "desktop:/")
    } */

    //Create more panels for other screens
    if (i > 0){
        var panel = new Panel
        panel.screen = i
        panel.location = 'bottom'
        // panel.height = screenGeometry(i).height > 1024 ? 35 : 27
	panel.height = 48
        // var tasks = panel.addWidget("tasks")
        var tasks = panel.addWidget("icontasks")
        tasks.writeConfig("showOnlyCurrentScreen", true);
    }
}
