from config import Cfg
from near_multinode_rpc_provider import MultiNodeJsonProviderError,  MultiNodeJsonProvider
import json
import time

def get_proposal_voting_info(start_id, end_id):
    info = []

    try:
        conn = MultiNodeJsonProvider(Cfg.NETWORK_ID)
        for id in range(start_id, end_id+1):
            ret = conn.view_call(Cfg.NETWORK[Cfg.NETWORK_ID]["DAO_CONTRACT"], 
                "get_proposal", ('{"id": %s}' % id).encode('utf-8'))
            json_str = "".join([chr(x) for x in ret["result"]])
            # print(json_str)
            info.append(json.loads(json_str))
            time.sleep(0.5)
    except MultiNodeJsonProviderError as e:
        print("RPC Error: ", e)
    except Exception as e:
        print("Error: ", e)

    return info

def counting_voters(start_id, end_id):
    counting = {}
    info_list = get_proposal_voting_info(start_id, end_id)
    for info in info_list:
        for voter in info['votes'].keys():
            if voter in counting:
                counting[voter] += 1
            else:
                counting[voter] = 1
    return counting

if __name__ == '__main__':
    # a = get_proposal_voting_info(294)
    counting = counting_voters(268, 294)
    print(counting)