<!DOCTYPE html>
</html>
    <head>
        <meta charset="utf-8">
        <title>Individual Dashboard</title>
        <script type="text/javascript" src="d3/d3.v3.js">
		
		
		</script>
		
		
		
		<style type="text/css">
			

		body {
		  font: 10px sans-serif;
		}

		.axis path,
		.axis line {
		  fill: none;
		  stroke: #000;
		  shape-rendering: crispEdges;
		}

		.x.axis path {
		  display: none;
		}

		.line {
		  fill: none;
		  stroke: steelblue;
		  stroke-width: 1.5px;
		}


		</style>
		
			
		
    </head>
    
	
	<div style="text-align: center;">
    <img class="banner" src="images/logo.png"/>
</div>

		
		
	
	
	
		<div align="right">
			<select id="yeardropdown">
			<option value="2009"  >2009</option>
			<option value="2010" selected>2010</option>
			<option value="2011">2011</option>
			<option value="2012">2012</option>
			<option value="2013">2013</option>
			</select>
			
			<div align="right">
			<select id="locationdropdown">
			<option value="Cali">Cali</option>
			<option value="Beijing" selected>Beijing</option>
			<option value="Pruszkow">Pruszkow</option>
			<option value="Astana">Astana</option>
			<option value="Copenhagen">Copenhagen</option>
			<option value="Manchester">Manchester</option>
			<option value="Melbourne">Melbourne</option>
			</select>
			
			<div align="right">
			<select id="genderdropdown">
			<option value="Mens" selected>Mens</option>
			<option value="Womens">Womens</option>
			</select>
			
			<div align="right">
			<select id="eventdropdown">
			<option value="IndividualPursuit">IndividualPursuit</option>
			<option value="TeamPursuit">TeamPursuit</option>
			<option value="TeamSprint" selected>TeamSprint</option>
			<option value="Kilometer">Kilometer</option>
			</select>
			
			<form><input type=button value="Submit" onClick="history.go()"></form> 
			
			<script>
			
			</script>
			
		
	
	
		<body>
        <script type="text/javascript">
		
		var filenamelist = ['2009WorldChampionshipsPruszkowMensIndividualPursuitQualifying', '2009WorldChampionshipsPruszkowMensKilometer', '2009WorldChampionshipsPruszkowMensTeamPursuitFinal', '2009WorldChampionshipsPruszkowMensTeamPursuitQualifying', '2009WorldChampionshipsPruszkowMensTeamSprintFinal', '2009WorldChampionshipsPruszkowMensTeamSprintQualifying', '2009WorldChampionshipsPruszkowWomensIndividualPursuitFinal', '2009WorldChampionshipsPruszkowWomensIndividualPursuitQualifying', '2009WorldChampionshipsPruszkowWomensTeamPursuitFinal', '2009WorldChampionshipsPruszkowWomensTeamPursuitQualifying', '2009WorldChampionshipsPruszkowWomensTeamSprintFinal', '2009WorldChampionshipsPruszkowWomensTeamSprintQualifying', '2009WorldCupBeijingMensIndividualPursuitFinal', '2009WorldCupBeijingMensIndividualPursuitQualifying', '2009WorldCupBeijingMensKilometer', '2009WorldCupBeijingMensTeamPursuitFinal', '2009WorldCupBeijingMensTeamPursuitQualifying', '2009WorldCupBeijingMensTeamSprintFinal', '2009WorldCupBeijingMensTeamSprintQualifying', '2009WorldCupBeijingWomensIndividualPursuitFinal', '2009WorldCupBeijingWomensIndividualPursuitQualifying', '2009WorldCupBeijingWomensTeamPursuitFinal', '2009WorldCupBeijingWomensTeamPursuitQualifying', '2009WorldCupBeijingWomensTeamSprintFinal', '2009WorldCupBeijingWomensTeamSprintQualifying', '2009WorldCupCaliMensIndividualPursuitFinal', '2009WorldCupCaliMensIndividualPursuitQualifying', '2009WorldCupCaliMensKilometer', '2009WorldCupCaliMensTeamPursuitFinal', '2009WorldCupCaliMensTeamPursuitQualifying', '2009WorldCupCaliMensTeamSprintFinal', '2009WorldCupCaliMensTeamSprintQualifying', '2009WorldCupCaliWomensIndividualPursuitFinal', '2009WorldCupCaliWomensIndividualPursuitQualifying', '2009WorldCupCaliWomensTeamPursuitFinal', '2009WorldCupCaliWomensTeamPursuitQualifying', '2009WorldCupCaliWomensTeamSprintFinal', '2009WorldCupCaliWomensTeamSprintQualifying', '2009WorldCupCopenhagenMensIndividualPursuitFinal', '2009WorldCupCopenhagenMensIndividualPursuitQualifying', '2009WorldCupCopenhagenMensKilometer', '2009WorldCupCopenhagenMensTeamPursuitFinal', '2009WorldCupCopenhagenMensTeamPursuitQualifying', '2009WorldCupCopenhagenMensTeamSprintFinal', '2009WorldCupCopenhagenMensTeamSprintQualifying', '2009WorldCupCopenhagenWomensIndividualPursuitFinal', '2009WorldCupCopenhagenWomensIndividualPursuitQualifying', '2009WorldCupCopenhagenWomensTeamPursuitFinal', '2009WorldCupCopenhagenWomensTeamPursuitQualifying', '2009WorldCupCopenhagenWomensTeamSprintFinal', '2009WorldCupCopenhagenWomensTeamSprintQualifying', '2009WorldCupManchesterMensIndividualPursuitFinal', '2009WorldCupManchesterMensIndividualPursuitQualifying', '2009WorldCupManchesterMensKilometer', '2009WorldCupManchesterMensTeamPursuitFinal', '2009WorldCupManchesterMensTeamPursuitQualifying', '2009WorldCupManchesterMensTeamSprintFinal', '2009WorldCupManchesterMensTeamSprintQualifying', '2009WorldCupManchesterWomensIndividualPursuitFinal', '2009WorldCupManchesterWomensIndividualPursuitQualifying', '2009WorldCupManchesterWomensTeamPursuitFinal', '2009WorldCupManchesterWomensTeamPursuitQualifying', '2009WorldCupManchesterWomensTeamSprintFinal', '2009WorldCupManchesterWomensTeamSprintQualifying', '2009WorldCupMelbourneMensIndividualPursuitFinal', '2009WorldCupMelbourneMensIndividualPursuitQualifying', '2009WorldCupMelbourneMensKilometer', '2009WorldCupMelbourneMensTeamPursuitFinal', '2009WorldCupMelbourneMensTeamPursuitQualifying', '2009WorldCupMelbourneMensTeamSprintFinal', '2009WorldCupMelbourneMensTeamSprintQualifying', '2009WorldCupMelbourneWomensIndividualPursuitFinal', '2009WorldCupMelbourneWomensIndividualPursuitQualifying', '2009WorldCupMelbourneWomensTeamPursuitFinal', '2009WorldCupMelbourneWomensTeamPursuitQualifying', '2009WorldCupMelbourneWomensTeamSprintFinal', '2009WorldCupMelbourneWomensTeamSprintQualifying', '2010WorldChampionshipMensIndividualPursuitFinal', '2010WorldChampionshipMensIndividualPursuitQualifying', '2010WorldChampionshipMensKilometer', '2010WorldChampionshipMensTeamPursuitFinal', '2010WorldChampionshipMensTeamPursuitQualifying', '2010WorldChampionshipMensTeamSprintFinal', '2010WorldChampionshipMensTeamSprintQualifying', '2010WorldChampionshipWomensIndividualPursuitFinal', '2010WorldChampionshipWomensIndividualPursuitQualifying', '2010WorldChampionshipWomensTeamPursuitFinal', '2010WorldChampionshipWomensTeamPursuitQualifying', '2010WorldChampionshipWomensTeamSprintFinal', '2010WorldChampionshipWomensTeamSprintQualifying', '2010WorldCupBeijingIndividualPursuitFinal', '2010WorldCupBeijingMensIndividualPursuitFinal', '2010WorldCupBeijingMensKilometer', '2010WorldCupBeijingMensTeamPursuitFinal', '2010WorldCupBeijingMensTeamPursuitQualifying', '2010WorldCupBeijingMensTeamSprintFinal', '2010WorldCupBeijingMensTeamSprintQualifying', '2010WorldCupBeijingWomensIndividualPursuitFinal', '2010WorldCupBeijingWomensIndividualPursuitQualifying', '2010WorldCupBeijingWomensTeamPursuitFinal', '2010WorldCupBeijingWomensTeamPursuitQualifying', '2010WorldCupBeijingWomensTeamSprintFinal', '2010WorldCupBeijingWomensTeamSprintQualifying', '2010WorldCupCaliMensTeamPursuitFinal', '2010WorldCupCaliMensTeamPursuitQualifying', '2010WorldCupCaliMensTeamSprintFinal', '2010WorldCupCaliMensTeamSprintQualifying', '2010WorldCupCaliWomensIndividualPursuitFinal', '2010WorldCupCaliWomensIndividualPursuitQualifying', '2010WorldCupCaliWomensTeamPursuitFinal', '2010WorldCupCaliWomensTeamPursuitQualifying', '2010WorldCupCaliWomensTeamSprintFinal', '2010WorldCupCaliWomensTeamSprintQualifying', '2010WorldCupMelbourneMensTeamPursuitFinal', '2010WorldCupMelbourneMensTeamPursuitQualifying', '2010WorldCupMelbourneMensTeamSprintFinal', '2010WorldCupMelbourneMensTeamSprintQualifying', '2010WorldCupMelbourneWomensTeamPursuitFinal', '2010WorldCupMelbourneWomensTeamPursuitQualifying', '2010WorldCupMelbourneWomensTeamSprintFinal', '2010WorldCupMelbourneWomensTeamSprintQualifying', '2011WorldChampionshipMenKilometer', '2011WorldChampionshipMensIndividualPursuitFinal', '2011WorldChampionshipMensIndividualPursuitQualifying', '2011WorldChampionshipMensTeamPursuitFinal', '2011WorldChampionshipMensTeamPursuitQualifying', '2011WorldChampionshipMensTeamSprintFinal', '2011WorldChampionshipMensTeamSprintQualifying', '2011WorldChampionshipWomensIndividualPursuitFinal', '2011WorldChampionshipWomensIndividualPursuitQualifying', '2011WorldChampionshipWomensTeamPursuitFinal', '2011WorldChampionshipWomensTeamPursuitQualifying', '2011WorldChampionshipWomensTeamSprintFinal', '2011WorldChampionshipWomensTeamSprintQualifying', '2011WorldCupAstanaMensIndividualPursuitFinal', '2011WorldCupAstanaMensIndividualPursuitQualifying', '2011WorldCupAstanaMensTeamPursuitFinal', '2011WorldCupAstanaMensTeamPursuitQualifying', '2011WorldCupAstanaMensTeamSprintFinal', '2011WorldCupAstanaWomensTeamPursuitFinal', '2011WorldCupAstanaWomensTeamPursuitQualifying', '2011WorldCupAstanaWomensTeamSprintFinal', '2011WorldCupAstanaWomensTeamSprintQualifying', '2011WorldCupBeijingMensTeamPursuitFinal', '2011WorldCupBeijingMensTeamPursuitQualifying', '2011WorldCupBeijingMensTeamSprintFinal', '2011WorldCupBeijingMensTeamSprintQualifying', '2011WorldCupBeijingWomensTeamPursuitFinal', '2011WorldCupBeijingWomensTeamPursuitQualifying', '2011WorldCupBeijingWomensTeamSprintQualifying', '2011WorldCupCaliMenKilometer', '2011WorldCupCaliMensTeamPursuitFinal', '2011WorldCupCaliMensTeamPursuitQualifying', '2011WorldCupCaliMensTeamSprintFinal', '2011WorldCupCaliMensTeamSprintQualifying', '2011WorldCupCaliWomensIndividualPursuitFinal', '2011WorldCupCaliWomensIndividualPursuitQualifying', '2011WorldCupCaliWomensTeamPursuitQualifying', '2011WorldCupCaliWomensTeamSprintFinal', '2011WorldCupCaliWomensTeamSprintQualifying', '2011WorldCupManchesterMensIndividualPursuitFinal', '2011WorldCupManchesterMensIndividualPursuitQualifying', '2011WorldCupManchesterMensTeamPursuitFinal', '2011WorldCupManchesterMensTeamPursuitQualifying', '2011WorldCupManchesterMensTeamSprintFinal', '2011WorldCupManchesterMensTeamSprintQualifying', '2011WorldCupManchesterWomensTeamPursuitFinal', '2011WorldCupManchesterWomensTeamPursuitQualifying', '2011WorldCupManchesterWomensTeamSprintFinal', '2011WorldCupManchesterWomensTeamSprintQualifying', '2012WorldChampionshipsMelbourneMensIndividualPursuitFinal', '2012WorldChampionshipsMelbourneMensIndividualPursuitQualifying', '2012WorldChampionshipsMelbourneMensKilometer', '2012WorldChampionshipsMelbourneMensTeamPursuitFinal', '2012WorldChampionshipsMelbourneMensTeamPursuitQualifying', '2012WorldChampionshipsMelbourneMensTeamSprintFinal', '2012WorldChampionshipsMelbourneMensTeamSprintQualifying', '2012WorldChampionshipsMelbourneWomensIndividualPursuitFinal', '2012WorldChampionshipsMelbourneWomensIndividualPursuitQualifying', '2012WorldChampionshipsMelbourneWomensTeamPursuitFinal', '2012WorldChampionshipsMelbourneWomensTeamPursuitQualifying', '2012WorldChampionshipsMelbourneWomensTeamSprintFinal', '2012WorldChampionshipsMelbourneWomensTeamSprintQualifying', '2012WorldCupBeijingMensIndivdualPursuitQualifying', '2012WorldCupBeijingMensIndividualPursuitFinal', '2012WorldCupBeijingMensTeamPursuitFinal', '2012WorldCupBeijingMensTeamPursuitQualifying', '2012WorldCupBeijingMensTeamSprintFinal', '2012WorldCupBeijingMensTeamSprintQualifying', '2012WorldCupBeijingWomensTeamPursuitFinal', '2012WorldCupBeijingWomensTeamPursuitQualifying', '2012WorldCupBeijingWomensTeamSprintFinal', '2012WorldCupBeijingWomensTeamSprintQualifying', '2012WorldCupCaliMensKilometer', '2012WorldCupCaliMensTeamPursuitFinal', '2012WorldCupCaliMensTeamPursuitQualifying', '2012WorldCupCaliMensTeamSprintFinal', '2012WorldCupCaliMensTeamSprintQualifying', '2012WorldCupCaliWomensTeamPursuitFinal', '2012WorldCupCaliWomensTeamPursuitQualifying', '2012WorldCupCaliWomensTeamSprintFinal', '2012WorldCupCaliWomensTeamSprintQualifying', '2012WorldCupGlasgowMensIndividualPursuitFinal', '2012WorldCupGlasgowMensIndividualPursuitQualifying', '2012WorldCupGlasgowMensTeamPursuitFinal', '2012WorldCupGlasgowMensTeamPursuitQualifying', '2012WorldCupGlasgowMensTeamSprintFinal', '2012WorldCupGlasgowMensTeamSprintQualifying', '2012WorldCupGlasgowWomensTeamPursuitFinal', '2012WorldCupGlasgowWomensTeamPursuitQualifying', '2012WorldCupGlasgowWomensTeamSprintFinal', '2012WorldCupGlasgowWomensTeamSprintQualifying', '2012WorldCupLondonMensKilometer', '2012WorldCupLondonMensTeamPursuitFinal', '2012WorldCupLondonMensTeamPursuitQualifying', '2012WorldCupLondonMensTeamSprintFinal', '2012WorldCupLondonMensTeamSprintQualifying', '2012WorldCupLondonWomensIndividualPursuitQualifying', '2012WorldCupLondonWomensTeamPursuitFinal', '2012WorldCupLondonWomensTeamPursuitQualifying', '2012WorldCupLondonWomensTeamSprintFinal', '2012WorldCupLondonWomensTeamSprintQualifying', '2013WorldChampionshipsMensIndividualPursuitFinal', '2013WorldChampionshipsMensIndividualPursuitQualifying', '2013WorldChampionshipsMensKilometer', '2013WorldChampionshipsMensTeamPursuitFinal', '2013WorldChampionshipsMensTeamPursuitQualifying', '2013WorldChampionshipsMensTeamSprintFinal', '2013WorldChampionshipsMensTeamSprintQualifying', '2013WorldChampionshipsWomensIndividualPursuitFinal', '2013WorldChampionshipsWomensIndividualPursuitQualifying', '2013WorldChampionshipsWomensTeamPursuitFinal', '2013WorldChampionshipsWomensTeamPursuitQualifying', '2013WorldChampionshipsWomensTeamSprintFinal', '2013WorldChampionshipsWomensTeamSprintQualifying', '2013WorldUCICupMensTeamPursuitFinal', '2013WorldUCICupMensTeamPursuitQualifying', '2013WorldUCICupMensTeamSprintFinal', '2013WorldUCICupMensTeamSprintQualifying', '2013WorldUCICupsWomensTeamPursuitQualifying', '2013WorldUCICupWomensIndividualPursuitFinal', '2013WorldUCICupWomensIndividualPursuitQualifying', '2013WorldUCICupWomensTeamPursuitFinal', '2013WorldUCICupWomensTeamSprintFinal', '2013WorldUCICupWomensTeamSprintQualifying']
		
		
		
		var margin = {top: 20, right: 80, bottom: 50, left: 50},
			width = 960 - margin.left - margin.right,
			height = 550 - margin.top - margin.bottom;
			
		var x= d3.scale.linear()
			.range([0, width]);
	
		var y = d3.scale.linear()
			.range([height, 0]);
	
		var color = d3.scale.category10();
		
		var xAxis = d3.svg.axis()
			.scale(x)
			.orient("bottom");

		var yAxis = d3.svg.axis()
			.scale(y)
			.orient("left");

		var line = d3.svg.line()
			.interpolate("basis")
			.x(function(d) { return x(d.lap); })
			.y(function(d) { return y(d.place); });
			
		var svg = d3.select("body").append("svg")
			.attr("width", width + margin.left + margin.right)
			.attr("height", height + margin.top + margin.bottom)
			.append("g")
			.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

		var getyear = document.getElementById("yeardropdown");
		var l = document.getElementById("locationdropdown");
		var g = document.getElementById("genderdropdown");
		var e = document.getElementById("eventdropdown");
			
		var filename = filenamelist[1];
		var yearShow = getyear.options[getyear.selectedIndex].text;
		var locationShow = l.options[l.selectedIndex].text;
		var genderShow = g.options[g.selectedIndex].text;
		var eventShow = e.options[e.selectedIndex].text;
		var typeShow = "Qualifying";
		
		var change = false;
		for(var i =0; i<filenamelist.length; i++){
			if((filenamelist[i].indexOf(yearShow) > -1) && (filenamelist[i].indexOf(locationShow) > -1)&& (filenamelist[i].indexOf(genderShow) > -1) && (filenamelist[i].indexOf(eventShow) > -1) && (filenamelist[i].indexOf(typeShow) > -1)){
				filename = filenamelist[i];
				change = true;
				}
		}
		
		if(change === false){
			alert("Sorry! That event does not exist.");
		}
		
		d3.csv("IndividualRaceDashboardData\\"+filename+".csv", function(data){
			color.domain(d3.keys(data[0]).filter(function(key) { return key !== "lap"; }));
			
			
			
			var teams = color.domain().map(function(name) {
				return {
					name: name,
					values: data.map(function(d) {
						return {lap: d.lap, place: +d[name]};
						  })
						};
					  });
					  
					  x.domain(d3.extent(data, function(d) { return d.lap; }));

					  y.domain([
						d3.min('0'),
						//d3.min(teams, function(c) { return d3.min(c.values, function(v) { return v.place; }); }),
						d3.max(teams, function(c) { return d3.max(c.values, function(v) { return v.place; }); })
					  ]);

					  svg.append("g")
						  .attr("class", "x axis")
						  .attr("text-anchor", "middle")
						  .attr("transform", "translate(0," + height + ")")
						  .call(xAxis)
						  .append("text")
						  .attr("x", width/2)
						  .attr("y", 30 )
						  
						  .text("Lap");

					  svg.append("g")
						  .attr("class", "y axis")
						  .call(yAxis)
						.append("text")
						  .attr("transform", "rotate(-90)")
						  .attr("y", 6)
						  .attr("dy", ".71em")
						  .style("text-anchor", "end")
						  .text("Place");

					  var team = svg.selectAll(".team")
						  .data(teams)
						.enter().append("g")
						  .attr("class", "team");

					  team.append("path")
						  .attr("class", "line")
						  .attr("d", function(d) { return line(d.values); })
						  .style("stroke", function(d) { return color(d.name); });

					  team.append("text")
						  .datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; })
						  .attr("transform", function(d) { return "translate(" + x(d.value.lap) + "," + y(d.value.place) + ")"; })
						  .attr("x", 3)
						  .attr("dy", ".35em")
						  .text(function(d) { return d.name; });
					});
							
						
		</script>
		  </body>
</html>
