function requestData(){$.ajax({url:session_url,success:function(t){var e=$("#points").highcharts();e.xAxis[0].setCategories(t.committees,!1),e.series[0].setData(t.drs,!1),e.series[1].setData(t.points,!1),e.redraw(),$("#total_points").html("Total Points: "+t.total_points),$("#total_type").html("("+t.type_point+" Points, "+t.type_dr+" Direct Responses)"),$("#mpp").html("Minutes Per Point: "+t.mpp),setTimeout(requestData,2e3)},cache:!1})}var chart_points;$(document).ready(function(){var t=$(".debates");t.masonry({itemSelector:".debate-box",columnWidth:".debate-box",transitionDuration:0}),chart_points=new Highcharts.Chart({chart:{renderTo:"points",defaultSeriesType:"column",backgroundColor:"#fff",events:{load:requestData}},title:!1,xAxis:{categories:[]},yAxis:{min:0,title:{text:"Number of Points"},stackLabels:{enabled:!0,style:{fontWeight:"bold",color:Highcharts.theme&&Highcharts.theme.textColor||"gray"}}},credits:{enabled:!1},legend:{align:"right",x:-30,verticalAlign:"top",y:25,floating:!0,backgroundColor:Highcharts.theme&&Highcharts.theme.background2||"white",borderColor:"#CCC",borderWidth:1,shadow:!1},tooltip:{formatter:function(){return"<b>"+this.x+"</b><br/>"+this.series.name+": "+this.y+"<br/>Total: "+this.point.stackTotal}},plotOptions:{column:{stacking:"normal",dataLabels:{enabled:!1,color:Highcharts.theme&&Highcharts.theme.dataLabelsColor||"white",style:{textShadow:"0 0 3px black"}}}},series:[{name:"Direct Response",data:[],color:"#F44336"},{name:"Point",data:[],color:"#3F51B5"}]})});