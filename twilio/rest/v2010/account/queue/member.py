# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import InstanceResource
from twilio.rest.resources.base import ListResource


class Member(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: call_sid
    
        A 34 character string that uniquely identifies the call that is
        enqueued.
    
    .. attribute:: date_enqueued
    
        The date that the member was enqueued, given in RFC 2822 format.
    
    .. attribute:: parent_sid
    
        The parent_sid
    
    .. attribute:: position
    
        This member's current position in the queue.
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: uri
    
        The uri
    
    .. attribute:: wait_time
    
        The number of seconds the member has been in the queue.
    """
    id_key = "call_sid"

    def load(self, *args, **kwargs):
        super(Member, self).load(*args, **kwargs)
        
        if hasattr(self, "date_enqueued") and self.date_enqueued:
            self.date_enqueued = parse_iso_date(self.date_enqueued)

    def update(self, **kwargs):
        """
        Dequeue a member from a queue and have the member's call begin executing the TwiML document at that URL
        
        :param str method: The method
        :param str url: The url
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Member`
        """
        return self.update_instance(kwargs)

    def dequeue(self, url, method='POST', **kwargs):
        """ An alias to update """
        return self.update(url=url, method=method, **kwargs)


class Members(ListResource):
    name = "Members"
    mount_name = "members"
    key = "queue_members"
    instance = Member

    def __init__(self, *args, **kwargs):
        super(Members, self).__init__(*args, **kwargs)

    def get(self, call_sid):
        """
        Fetch a specific members of the queue
        
        :param str call_sid: The call_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Member`
        :returns: A placeholder for a :class:`Member` resource
        """
        return self.get_instance(call_sid)

    def update(self, call_sid, url, method, **kwargs):
        """
        Dequeue a member from a queue and have the member's call begin executing the TwiML document at that URL
        
        :param str call_sid: The call_sid
        :param str method: The method
        :param str url: The url
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Member`
        """
        kwargs["Url"] = url
        kwargs["Method"] = method
        return self.update_instance(call_sid, kwargs)

    def list(self, **kwargs):
        """
        Retrieve a list of members in the queue
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Member`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of members in the queue
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Member`
        """
        return super(Members, self).iter(**kwargs)

    def dequeue(self, sid, url, method='POST', **kwargs):
        """ An alias to update """
        return self.update(sid, url=url, method=method, **kwargs)
