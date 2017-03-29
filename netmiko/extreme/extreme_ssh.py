"""Extreme support."""
from __future__ import unicode_literals
import string
from netmiko.cisco_base_connection import CiscoSSHConnection


class ExtremeSSH(CiscoSSHConnection):
    """Extreme support."""
    def session_preparation(self):
        """Extreme requires enable mode to disable paging."""
        self._test_channel_read()
        self.enable()
        self.set_base_prompt()
        self.disable_paging(command="disable clipaging\n")

    def set_base_prompt(self, pri_prompt_terminator='#', alt_prompt_terminator='>', delay_factor=1):
        super(ExtremeSSH, self).set_base_prompt(pri_prompt_terminator,alt_prompt_terminator, delay_factor)        
        if self.base_prompt:
            self.base_prompt = self.base_prompt.strip().rstrip(string.digits)
        return self.base_prompt
