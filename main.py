import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction

logger = logging.getLogger(__name__)

CMD_LOCKSCREEN = '''dbus-send --type=method_call --dest=org.gnome.ScreenSaver \
        /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock'''

class ScreenLockerExtension(Extension):

    def __init__(self):
        super(ScreenLockerExtension, self).__init__()
        logger.info('Executing lock screen command')
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Lock screen',
                                         on_enter=RunScriptAction(CMD_LOCKSCREEN, [])))

        return RenderResultListAction(items)

if __name__ == '__main__':
    ScreenLockerExtension().run()