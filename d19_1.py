import re

tri_nums = [(x-1)*x//2 for x in range(25)]

def dfs(timeleft, robot, r_ore, r_clay, r_obs, r_geo, ore, clay, obs, geo):
    global geodes
    if (
        robot == 0 and r_ore >= m_ore
        or robot == 1 and r_clay >= m_clay
        or robot == 2 and (r_obs >= m_obs or r_clay == 0)
        or robot == 3 and r_obs == 0
        or geo + r_geo * timeleft + tri_nums[timeleft] <= geodes
    ):
        return
    while timeleft:
        if robot == 0 and ore >= r_ore_ore:
            for robot in range(4):
                dfs(
                    timeleft - 1, robot, r_ore + 1,
                    r_clay, r_obs, r_geo, ore - r_ore_ore + r_ore,
                    clay + r_clay, obs + r_obs, r_geo + geo,
                )
            return
        elif robot == 1 and ore >= r_clay_ore:
            for robot in range(4):
                dfs(
                    timeleft - 1, robot, r_ore,
                    r_clay + 1, r_obs, r_geo, ore - r_clay_ore + r_ore,
                    clay + r_clay, obs + r_obs, r_geo + geo,
                )
            return
        elif robot == 2 and ore >= r_obs_ore and clay >= r_obs_clay:
            for robot in range(4):
                dfs(
                    timeleft - 1, robot, r_ore,
                    r_clay, r_obs + 1, r_geo, ore - r_obs_ore + r_ore,
                    clay - r_obs_clay + r_clay, obs + r_obs, r_geo + geo,
                )
            return
        elif robot == 3 and ore >= r_geo_ore and obs >= r_geo_obs:
            for robot in range(4):
                dfs(
                    timeleft - 1, robot, r_ore,
                    r_clay, r_obs, r_geo + 1, ore - r_geo_ore + r_ore,
                    clay + r_clay, obs - r_geo_obs + r_obs, r_geo + geo,
                )
            return
        timeleft, ore, clay, obs, geo = timeleft - 1, ore + r_ore, clay + r_clay, obs + r_obs, geo + r_geo
    geodes = max(geodes, geo)


quality_levels = 0
while inp := input():
    n, r_ore_ore, r_clay_ore, r_obs_ore, r_obs_clay, r_geo_ore, r_geo_obs = (*map(
        int, re.findall("\d+", inp)
    ),)
    m_ore, m_clay, m_obs = (
        max(r_ore_ore, r_clay_ore, r_obs_ore, r_geo_ore),
        r_obs_clay,
        r_geo_obs,
    )
    geodes = 0
    for robot in range(4):
        dfs(24, robot, 1, 0, 0, 0, 0, 0, 0, 0)
    quality_levels += geodes * n

print(quality_levels)
