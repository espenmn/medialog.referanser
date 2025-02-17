# -*- coding: utf-8 -*-

# from medialog.referanser import _
from Products.Five.browser import BrowserView
from zope.interface import Interface

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class IReferanserView(Interface):
    """ Marker Interface for IReferanserView"""


class ReferanserView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('referanser_view.pt')

    def __call__(self):
        # Implement your own actions:
        return self.index()
