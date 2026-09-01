# Copyright (c) 2014 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

from __future__ import absolute_import

import sys

import sgtk
from sgtk.platform.qt import QtCore, QtGui

if sys.version_info.major == 2:
    from .ui_python2.submit_dialog import Ui_SubmitDialog
else:
    from .ui.submit_dialog import Ui_SubmitDialog


class SubmitDialog(QtGui.QWidget):
    """
    Main UI dialog for the custom Shot Export. This will
    give the user an overview of what is going to happen,
    ask the user to enter comments and choose an export preset
    for the generated plates.
    """

    def __init__(self, presets, publish_source_element_default=False):
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)

        # now load in the UI that was created in the UI designer
        self.ui = Ui_SubmitDialog()
        self.ui.setupUi(self)

        # with the tk dialogs, we need to hook up our modal
        # dialog signals in a special way
        self.__exit_code = QtGui.QDialog.Rejected
        self.ui.submit.clicked.connect(self._on_submit_clicked)
        self.ui.cancel.clicked.connect(self._on_cancel_clicked)

        # load up the export presets
        self.ui.export_presets.addItems(presets)

        self.ui.publish_source_element.setChecked(publish_source_element_default)

    @property
    def exit_code(self):
        """
        Used to pass exit code back though sgtk dialog

        :returns:    The dialog exit code
        """
        return self.__exit_code

    def get_comments(self):
        """
        Returns the comments entered by the user
        """
        return self.ui.comments.toPlainText()

    def get_video_preset(self):
        """
        Returns the name of the selected video preset
        """
        return self.ui.export_presets.currentText()

    def get_publish_source_element(self):
        """
        Returns True if the user has chosen to publish source media as a ShotGrid Element
        """
        return self.ui.publish_source_element.isChecked()

    def _on_submit_clicked(self):
        """
        Called when the 'submit' button is clicked.
        """

        # # Debug with debugpy by uncommenting the following lines
        # import debugpy

        # # 5678 is the default attach port in the VS Code debug configurations. Unless a host and port are specified, host defaults to 127.0.0.1
        # debugpy.log_to("~/debugpy.log")
        # debugpy.configure(python="/opt/Shotgun/Python3/bin/python")
        # debugpy.listen(5678)
        # debugpy.wait_for_client()
        # debugpy.breakpoint()

        self.__exit_code = QtGui.QDialog.Accepted
        self.close()

    def _on_cancel_clicked(self):
        """
        Called when the 'cancel' button is clicked.
        """
        self.__exit_code = QtGui.QDialog.Rejected
        self.close()
