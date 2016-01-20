# Cluster Assisted Magical Wand

### Members:
* Lucas Merlette
* Lyoma Guillou



## How does the neural_network algorithm work ?

### Important files
* src/neural_network/super_neuron.py
* src/neural_network/neuron.py

### Super Neuron algorithm

#### super_neuron.__init__
Initializes the variables:

* ***self.image*** is the image as a list of list containing tuples: image[y][x] = (0->255, 0->255, 0->255)
* ***self.image_size*** is the image size as a tuple: (y, x)
* ***self.color_histogram*** is the color histogram
* ***self.imploded_image*** is a copy of the image when neurons are merged (Useless for now)
* ***self.neurons*** is a list of neurons, a neuron being a cluster

Algorithm:
For each pixel in the image given in parameter, create a neuron.
There will be (image.y * image.x) neurons at the end of the super_neuron.__init__ method.

for y in image.y
    for x in image.x
    	self.neurons.append(Neuron(image[y][x], y, x))


#### super_neuron.merge_neighbour_neurons
Merges the neurons that are neighbours and have the same pixel value

Simplified algorithm:

for i in len(self.neurons)
    if i >= len(self.neurons)
       break
    neuron = self.neurons[i]
    boundaries = neuron.get_boundaries()
    if boundaries == []
       return None
    for other_neuron in self.neurons
    	if other_neuron == neuron
	   continue
	for boundary in boundaries:
	    if boundary_in_neuron(other_neuron, boundary)
	       if other_neuron.get_color() == neuron.get_color()
	       	  merge_neurons(neuron, other_neuron)

Explanation:

We loop on the neurons, and for each neuron, we get its boundaries (a list of dictionaries containing the pixels on the boundaries of the neuron, because obviously only the pixels on boundaries have neighbour pixels from other neurons) of type list of dictionaries {'y': pixel_y, 'x': pixel_x, 'value': pixel}.
For each neuron, we loop on the other neurons (we avoid comparing the same neurons with the continue block) to compare their boundaries.
For each boundary of the currently selected neuron (selected in the first loop), we check if the boundary has neighbours in the other_neuron selected (selected in the second loop). If the boundary has neighbour pixels in the other_neuron, then we check if the value of the pixels (ie. the color) of the other_neuron is the same as the one from the currently selected neuron. If they have the same color, we proceed to the merging.
To merge two neurons, we simply add the other_neuron.image_segments to the currently selected neuron, and remove the other_neuron from the list of neurons of the super_neuron.
