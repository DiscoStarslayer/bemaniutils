# vim: set fileencoding=utf-8
from typing import Optional

from bemani.backend.ddr.base import DDRBase
from bemani.backend.ddr.ddrace import DDRAce
from bemani.common import VersionConstants, CardCipher
from bemani.protocol import Node


class DDRA20(
    DDRAce,
    DDRBase,
):
    name: str = "DanceDanceRevolution A20"
    version: int = VersionConstants.DDR_A20

    def previous_version(self) -> Optional[DDRBase]:
        return DDRAce(self.data, self.config, self.model)

    @property
    def supports_paseli(self) -> bool:
        if self.model.dest != "J":
            # DDR Ace in USA mode doesn't support PASELI properly.
            # When in Asia mode it shows PASELI but won't let you select it.
            return False
        else:
            # All other modes should work with PASELI.
            return True

    # def handle_eventlog_write_request(self, request: Node) -> Node:
    #     root = Node.void("eventlog")
    #
    #     root.add_child(Node.s64("gamesession", 1))
    #     root.add_child(Node.s32("logsendflg", 0))
    #     root.add_child(Node.s32("logerrlevel", 0))
    #     root.add_child(Node.s32("evtidnosendflg", 0))
    #
    #     return root
    #
    #
    # def handle_system_convcardnumber_request(self, request: Node) -> Node:
    #     card_id = request.child_value("data/card_id")
    #     card_number = CardCipher.encode(card_id)
    #
    #     system = Node.void("system")
    #     data = Node.void("data")
    #     system.add_child(data)
    #
    #     system.add_child(Node.s32("result", 0))
    #     data.add_child(Node.string("card_number", card_number))
    #     return system
