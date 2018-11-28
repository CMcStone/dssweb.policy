from zope.interface import implements, Interface
from Products.CMFPlone import PloneMessageFactory as _
from plone.app.workflow.interfaces import ISharingPageRole as interfaceToImplement


from Products.CMFPlone import PloneMessageFactory as _


"""
Adding a contributor role to a special manage portlets role in the sharing tab
"""


class ManagePortletsRole(object):
    implements(interfaceToImplement)

    title = _(u"title_can_portlets", default=u"Manage Portlets")
    required_permission = "Sharing page: Manage Portlets"
