import os

def growth_threshold_reached(path, threshold):
    threshold_timepoints = []
    for i in range(160):
        filename = f"experiment_{i:03}.csv"
        filepath = os.path.join(path, filename)
        with open(filepath, 'r') as file:
            growth_values = list(map(float, file.readline().strip().split(',')))
            for idx, growth in enumerate(growth_values):
                if growth >= threshold:
                    threshold_timepoints.append(idx*10)
                    break
    average_timepoint = sum(threshold_timepoints) / len(threshold_timepoints)
    return average_timepoint

# Test the function
path = 'c:\\temp\\'
threshold = 8.5
average_timepoint = growth_threshold_reached(path, threshold)
print('The average timepoint at which the threshold was reached is', average_timepoint)
