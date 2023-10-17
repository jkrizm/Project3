// Create a custom function to return songs in the 50s
function selectfifties(name) {
    return name.decade == "1950";
  }
  
  // Call the custom function with filter()
  let fiftiessongs = final.filter(selectfifties);
  
  // Display the results
  console.log(fiftiessongs);
  

  // Sort the data by accoustic by ascending order
let sortedByacousticness= final.sort((a, b) => b.acousticness- a.acousticness);



// Reverse the array to accommodate Plotly's defaults
fiftiessongs.reverse();

// Trace1 for the accoustic Data. make the graph horizontal with the largest category at the top
let trace1 = {
  x: fiftiessongs.map(object => object.id),
  y: fiftiessongs.map(object => object.acousticness),
  text: fiftiessongs.map(object => object.id),
  name: "id",
  type: "scatter",
  orientation: "v"
};

// Data array
let data = [trace1];

// Apply a title to the layout
let layout = {
  title: "50s songs acousticness",
  margin: {
    l: 100,
    r: 100,
    t: 100,
    b: 100
  }
};

// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);
