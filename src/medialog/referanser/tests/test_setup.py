# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from medialog.referanser.testing import MEDIALOG_REFERANSER_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that medialog.referanser is properly installed."""

    layer = MEDIALOG_REFERANSER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if medialog.referanser is installed."""
        self.assertTrue(self.installer.is_product_installed(
            'medialog.referanser'))

    def test_browserlayer(self):
        """Test that IMedialogReferanserLayer is registered."""
        from medialog.referanser.interfaces import (
            IMedialogReferanserLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IMedialogReferanserLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MEDIALOG_REFERANSER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstall_product('medialog.referanser')
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if medialog.referanser is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'medialog.referanser'))

    def test_browserlayer_removed(self):
        """Test that IMedialogReferanserLayer is removed."""
        from medialog.referanser.interfaces import \
            IMedialogReferanserLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMedialogReferanserLayer, utils.registered_layers())
