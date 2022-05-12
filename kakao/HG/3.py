import math
def solution(alp, cop, problems):
    answer = 0
    costs = [(1, 0, 1), (0, 1, 1)] # alp_rwd, cop_rwd, cost

    for problem in sorted(problems, key = lambda x : x[0] + x[1]):
        # print("=================")
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        # print(problem)
        # print(alp, cop)
        # print("alp")
        if alp < alp_req:
            need = alp_req - alp
            MIN = float('inf')
            choose = (0, 0, 0)
            tmp = 0
            for ar, cr, co in costs:
                if ar == 0:
                    continue
                tmp = math.ceil(need / ar)
                # print(tmp)
                if MIN == tmp * ar and (choose[0] + choose[1]) * choose[2] > (ar + cr) * co:
                    continue
                elif MIN >= tmp * ar:
                    # print("MIN :", ar, cr, co)
                    MIN = tmp * co
                    choose = (ar, cr, co)
            
            # print(MIN, choose)
            answer += MIN
            alp += choose[0] * tmp
            cop += choose[1] * tmp
        # print("cop")
        if cop < cop_req:
            need = cop_req - cop
            MIN = float('inf')
            choose = (0, 0)
            tmp = 0
            for ar, cr, co in costs:
                if cr == 0:
                    continue
                tmp = math.ceil(need / cr)
                # print(tmp)
                if MIN == tmp * co and (choose[0] + choose[1]) * choose[2] > (ar + cr) * co:
                    continue
                if MIN >= tmp * co:
                    # print("MIN :", ar, cr, co)
                    MIN = tmp * co
                    choose = (ar, cr)
            # print(MIN, choose)
            answer += MIN
            alp += choose[0] * tmp
            cop += choose[1] * tmp
        costs.append((alp_rwd, cop_rwd, cost))
        # print(alp, cop, answer, costs)
    return answer