from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

from cirb.urbis import urbisMessageFactory as _

import re, os
import urllib2, socket
from urllib2 import URLError, HTTPError

from zope.component import getUtility
from plone.registry.interfaces import IRegistry

class IUrbisView(Interface):
    """
    Cas view interface
    """

    def test():
        """ test method"""


class UrbisView(BrowserView):
    """
    Cas browser view
    """
    implements(IUrbisView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def urbis(self):
        """
        urbis method
        """
        registry = getUtility(IRegistry)
        ws_urbis = registry['cirb.urbis.urbis_url']
        error=False
        msg_error=''
        if not ws_urbis:
            error=True
            msg_error=_(u'No url for UrbIS map')
        return {'ws_urbis':ws_urbis,'error':error,'msg_error':msg_error}
