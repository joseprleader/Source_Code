from Point import Point
import sys

def main():
    
    ps0 = get_points_from_files(sys.argv[1])

    closest_points_dict = get_closest_points(ps0)

    result_str = "Closest 2 points are " + str(closest_points_dict["pa"]) + " and " + str(closest_points_dict["pb"]) + "."
    result_str += "\nThe distance is: " + str(closest_points_dict["distance"])

    print(result_str)

def get_closest_points(points_list):

    # Provisional list of distances
    distances = []

    # List of dictionaries of point a, point b, and the distance between them
    points_n_distances_dicts = []

    # Get list of indexes of points list
    points_indexes = get_indexes_from_list(points_list)

    # Get lowest and highest indexes
    lowest_index = min(points_indexes)
    highest_index = max(points_indexes)

    # Loop through each point
    for i in points_indexes:

        # Create a provisional iterator for previous points
        prov_i_for_prev = i

        # Create a provisional iterator for next points
        prov_i_for_next = i

        # As long as there are points before this point, get distances from them and add them to the distances list
        while prov_i_for_prev >= lowest_index:

            # Avoid getting distance for the same point
            if prov_i_for_prev < i:

                point_a = points_list[i]
                point_b = points_list[prov_i_for_prev]
                distance = point_a.get_distance_from(point_b)

                distances.append(distance)
                points_n_distances_dicts.append({"pa" : point_a, "pb": point_b, "distance" : distance})
            
            # Reduce the value of the iterator
            prov_i_for_prev -= 1
        
        # As long as there are points after this point, get distances from them and add them to the distances list
        while prov_i_for_next <= highest_index:

            # Avoid getting distance for the same point
            if prov_i_for_prev > i:

                point_a = points_list[i]
                point_b = points_list[prov_i_for_next]
                distance = point_a.get_distance_from(point_b)

                distances.append(distance)
                points_n_distances_dicts.append({"pa" : point_a, "pb": point_b, "distance" : distance})
            
            # Increase the value of the iterator
            prov_i_for_next += 1
        
    # Return list of dictionaries with point that has the lowest distance
    for point_dict in points_n_distances_dicts:

        if point_dict["distance"] == min(distances):
            
            if point_dict["pa"].x > point_dict["pb"].x:

                temp_x = point_dict["pa"].x
                temp_y = point_dict["pa"].y 

                point_dict["pa"].x = point_dict["pb"].x
                point_dict["pb"].x = temp_x

                point_dict["pa"].y = point_dict["pb"].y
                point_dict["pb"].y = temp_y
            
            return point_dict

def get_indexes_from_list(a_list):

    return [i for i in range(len(a_list))]

def get_points_from_files(file_name):

    points = []

    with open(file_name) as f:
        coors_list = f.read().split()
    
    x = None
    y = None

    for i in range(len(coors_list)):

        if i % 2 == 0:
            x = coors_list[i]
        
        else:
            y = coors_list[i]
            points.append(Point(x, y))
    
    return points

main()