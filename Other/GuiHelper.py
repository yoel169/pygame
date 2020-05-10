import pygame_gui
import pygame


# Helps make GUI elements like buttons, labels, and selections. Returns element.
class GuiHelper:

    def __init__(self, SW, SH, manager):
        self.SW = SW
        self.SH = SH
        self.manager = manager
        self.anchor = {'left': 'left', 'right': 'right', 'top': 'top', 'bottom': 'bottom'}

    def make_button(self, x, y, w, h, string, container):

        buttonSize = (0, 0, w, h)
        button_layout_rect = pygame.Rect(buttonSize)
        button_layout_rect.center = (x, y)

        if container is None:
            return pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                text=string, manager=self.manager)
        else:
            return pygame_gui.elements.UIButton(relative_rect=button_layout_rect,
                                                text=string, manager=self.manager,
                                                container=container)

    def make_label(self, x, y, w, h, string, id, container):

        labelSize = (0, 0, w, h)
        label_rect = pygame.Rect(labelSize)
        label_rect.center = (x, y)

        if id is None and container is None:
            return pygame_gui.elements.UILabel(relative_rect=label_rect, text=string,
                                               manager=self.manager)
        elif id is None and container is not None:
            return pygame_gui.elements.UILabel(relative_rect=label_rect, text=string,
                                               manager=self.manager,
                                               container=container)
        elif id is not None and container is not None:
            return pygame_gui.elements.UILabel(relative_rect=label_rect, text=string,
                                               manager=self.manager, object_id= id,
                                               container=container)
        else:
            return pygame_gui.elements.UILabel(relative_rect=label_rect, text=string,
                                               manager=self.manager, object_id= id)

    def make_selection_list(self, x, y, w, h, strings, id, container):

        selectionSize = (0, 0, w, h)
        dD_rect = pygame.Rect(selectionSize)
        dD_rect.center = (x, y)

        if container is None:
            return pygame_gui.elements.UISelectionList(dD_rect, strings, object_id=id,
                                                       manager=self.manager, allow_multi_select=False)
        else:
            return pygame_gui.elements.UISelectionList(dD_rect, strings, object_id=id,
                                                       manager=self.manager, allow_multi_select=False,
                                                       container=container)

    def make_panel(self, x, y, w, h, id):
        panel = (0, 0, w, h)
        panel_rect = pygame.Rect(panel)
        panel_rect.center = (x, y)

        return pygame_gui.elements.ui_panel.UIPanel(relative_rect=panel_rect, starting_layer_height=3,
                                                    manager=self.manager, object_id=id, anchors=self.anchor)

    def make_contained_panel(self, x, y, w, h, id, container):
        panel = (0, 0, w, h)
        panel_rect = pygame.Rect(panel)
        panel_rect.center = (x, y)

        return pygame_gui.elements.ui_panel.UIPanel(relative_rect=panel_rect, starting_layer_height=3,
                                                    manager=self.manager, object_id=id, container=container
                                                    , anchors=self.anchor)

    def make_drop_down_menu(self, x, y, w, h, id, stages):
        size = (0, 0, w, h)
        size_rect = pygame.Rect(size)
        size_rect.center = (x, y)

        if len(stages) == 0:
            stages = ['']

        return pygame_gui.elements.UIDropDownMenu(options_list=stages, starting_option=stages[0],
                                                  relative_rect=size_rect,
                                                  manager=self.manager, object_id=id)
