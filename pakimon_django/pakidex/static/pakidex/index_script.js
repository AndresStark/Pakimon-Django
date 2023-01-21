function selection(){
    var selector = document.getElementById("selector");
    var selection_text = selector.options[selector.selectedIndex].value;
    document.getElementById("text_selection").value = selection_text;
}