console.log("script")

  // this code will execute on page load
  // to populate the dropdown
function init(){
  let decade;
  d3.json("http://127.0.0.1:5000/api/by_decade").then(function(data) {
    decade = data;
    console.log(decade)
    
    for(x of data) {
      d3.select("#selDataset").append("option").attr("value", x.decade).text(x.decade)
    }
  
    histoplots(1950);

  });


};




// Plot the acousticness

function histoplots(myValue, attrib){
// // Display the results

d3.json("http://127.0.0.1:5000/api/all_data").then(function(data) {
// // Call the custom function with filter()
let dec_songs=[];
for (x of data) {
  if (x["decade"] == myValue)
  dec_songs.push(x)
};

console.log(dec_songs)

// Slice the first 10 objects for plotting
let slicedData = dec_songs.slice(0, 200);
// Reverse the array to accommodate Plotly's defaults
slicedData.reverse();
// Trace1 for the accoustic Data. make the graph horizontal with the largest category at the top
let trace1 = {
  x: slicedData.map(object => object[attrib]),
  autobinx: false,
  histnorm: "count",
  
  marker: {
    color: "rgb(30, 215, 93)",
     line: {
      color:  "rgb(0, 0, 0)",
      width: 1
    }
  },
  opacity: 1,
  type: "histogram",
};
// Data array
let data1 = [trace1];
// Apply a title to the layout
let layout = {
title: {
  text: myValue.toString() +"'s " +attrib,
  font:{
    color: "white",
  },
},
plot_bgcolor:"black",
paper_bgcolor:"black",
margin: {
  l: 30,
  r: 30,
  t: 30,
  b: 30
},
xaxis: {
  color: 'white'
},
yaxis: {
  color: 'white'
}};
// Render the plot to the div tag with id "plot"
Plotly.newPlot(attrib, data1, layout);
});
};


var sound = new Howl({
  src: ['https://p.scdn.co/mp3-preview/ab71015cd8957e29f04aadf38fb40741c8e2b711?cid=f4f54a850da14f27a6e2b44603fe8013'],
  format: ['mp3'],
  autoplay: true,
  loop: true,
  volume: 0.5,
});



function optionChanged(myValue){
  console.log(myValue)
  let attributes = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo','duration_ms', 'time_signature'];
  for (attrib of attributes){
    histoplots(myValue, attrib)
  };
  
};
init();

