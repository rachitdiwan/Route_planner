import math
import copy

def shortest_path(M,start,goal):
    print("shortest path called")
    cur_node = start
    cur_list =[str(cur_node)]
    cur_str = "-".join([str(cur_node)])
    travel_dict = {cur_str:calc_dist(M, start, goal)}
    goal_dict = {}
    g = 0
    count = 0
    while count<30:
        goal_dict = goal_dict_modifier(goal_dict, travel_dict, goal) 
        if len(goal_dict) != 0 and travel_dict[minimum(travel_dict)] >= goal_dict[minimum(goal_dict)]:
            break
        return_list_pair = frontier_calc(M, cur_node, g, goal, cur_list) 
        travel_dict = travel_dict_modifier(travel_dict, return_list_pair, cur_list) 
        cur_list = minimum(travel_dict).split("-")
        cur_node = int(cur_list[-1])
        f = travel_dict["-".join(cur_list)]
        g = f - calc_dist(M, cur_node, goal)
        count += 1
    return [int(val) for val in minimum(goal_dict).split("-")]

def calc_dist(Map, point1, point2):
    "returns distance between two points"
    [x1, y1] = Map.intersections[point1]
    [x2, y2] = Map.intersections[point2]
    distance = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    return distance

def travel_dict_modifier(dictionary, list_pairs, cur_list):
    "modifies the dictionary for the new frontiers"
    del dictionary["-".join(cur_list)]
    for val in list_pairs:
        cur_str = "-".join(cur_list + [val[0]])
        dictionary[cur_str] = val[1]
    return dictionary

def goal_dict_modifier(goal_dict, travel_dict, goal):
    "add an elements to goal dict if any path has reached the goal"
    key_list = travel_dict.keys()
    for val in key_list:
        val = val.split("-")
        if int(val[-1]) == goal:
            goal_dict["-".join(val)] = travel_dict["-".join(val)]
    return goal_dict

def minimum(dictionary):
    "returns the key with minimum value"
    min_index = 0
    val_list = list(dictionary.values())
    min_val = val_list[0]
    key_list = list(dictionary.keys())
    for i in range(len(val_list)):
        if min_val>val_list[i]:
            min_val = val_list[i]
            min_index = copy.copy(i)
    return key_list[min_index]
        

def frontier_calc(Map, node, g, goal, cur_list):
    "returns pair of neighbourhood nodes and their "f" values as 2D array"
    list_pairs = []
    for val in Map.roads[node]:
        if str(val) not in cur_list:
            dist_val = g + (calc_dist(Map, node, val)) + (calc_dist(Map, val, goal))
            list_pairs.append([str(val), dist_val])
    return list_pairs
     