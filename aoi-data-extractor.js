n = [];
$("table.data td.last a").each(function(){
    n.push($(this).attr("href"));
});
n = n.filter(function(d){ return d.indexOf("SSA") !== -1});
n.join("\n");
