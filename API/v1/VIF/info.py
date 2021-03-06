from fastapi import APIRouter

from XenXenXenSe.VIF import VIF
from XenXenXenSe.session import create_session

router = APIRouter()


@router.get("/{cluster_id}/vif/{vif_uuid}")
async def vif_get_by_uuid(cluster_id: str, vif_uuid: str):
    """ Get VIF by UUID """
    session = create_session(cluster_id)
    vif: VIF = VIF.get_by_uuid(session, vif_uuid)

    if vif is not None:
        ret = {"success": True, "data": vif.serialize()}
    else:
        ret = {"success": False}

    session.xenapi.session.logout()
    return ret
