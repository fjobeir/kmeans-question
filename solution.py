import numpy as np

points = np.array(eval(input()))
centroids = np.array(eval(input()))

#function returns the manhattan distance between points p1 and p2
def calc_dist(p1, p2):
    """p1 and p2 are two tuples representing the points"""
    
    dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    return dist
    
    
#function returns the updated centroid for the points in lst which represent a cluster
def update_centroid(lst):
    """lst is a 2d numpy array consisting of points in a cluster"""

    new_centroid = None
    
    #YOUR CODE GOES HERE
    val_x, val_y = 0, 0
    for x,y in lst:
        val_x += x
        val_y += y
        new_centroid = (np.round(val_x/len(lst), 2), np.round(val_y/len(lst), 2))
    return new_centroid
    
#function performs one iteration of k-means
def k_means(points, centroids):
    """points is a 2d numpy array consisting of points whereas
    centroids is a 2d numpy array consisting of initial centroids"""
       

    # clusters[i] stores all the points with the cluster label i
    clusters = [[] for i in range(len(centroids))]
    
    for pnt in points:
        #tmp[i] stores the distance of pnt from centroid[i]
        tmp = [0]*len(centroids) 
        for i,centroid in enumerate(centroids):
            tmp[i] = calc_dist(pnt, centroid)   #calculate the distance between point and centroid
        
        cluster_id = tmp.index(min(tmp))  #index of the centroid from which pnt is closest
        clusters[cluster_id].append(pnt)
        
    
    #update the centroid of each cluster
    new_centroid = []
    for cluster in clusters:
        new_centroid.append(update_centroid(cluster)) #update the centroid of cluster using update_centroid function we defined earlier
    
    return np.array(new_centroid)

for i in range(5):
    centroids = k_means(points, centroids)  #perform ith iteration on data to update clusters using k_means function we defined earlier
    print(np.round(centroids,2))