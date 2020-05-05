import pygame_gui
import pygame


# Helps make GUI elements like buttons, labels, and selections. Returns element.
class GuiHelper:

    def __init__(self, SW, SH, manager):
        self.SW = SW
        self.SH = SH
        self.manager = manager
        self.anchor = {'left': 'left', 'right': 'right', 'top': 'top', 'bottom': 'bottom'}

    def make_button(self, x, y, w, h, string):

        buttonSize = (0, 0, w, h)
        button_layout_rect = pygame.Rect(buttonSize)
        button_layout_rect.bottomright = (x, y)

        return pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                        text=string, manager=self.manager,
                                                        anchors=self.anchor)

    def make_label(self, x,y,w,h, string, id):

        labelSize = (0, 0, w, h)
        label_rect = pygame.Rect(labelSize)
        label_rect.bottomright = (x, y)

        return pygame_gui.elements.UILabel(relative_rect=label_rect, text=string,
                                             manager=self.manager, anchors=self.anchor, object_id= id)

    def make_selection_list(self, x,y,w,h, strings, id):

        selectionSize = (0, 0, w, h)
        dD_rect = pygame.Rect(selectionSize)
        dD_rect.bottomright = (x, y)

        return pygame_gui.elements.UISelectionList(dD_rect, strings, object_id=id,
                                                    manager=self.manager, allow_multi_select=False,
                                                                       anchors=self.anchor)