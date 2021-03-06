# Generating SLiM output

Generate output that can be read by this program by adding one of the following two options to your SLiM code:

##### OPTION 1. For slim code that uses colors that are strings, like "blue", "red", etc..
```C
//// SET OUTPUT PATH FOR VISUALIZATION FUNCTION:
1 early() {
    defineConstant("OUTPUT_PATH", getwd() + "/slim_movie");
    deleteFile(OUTPUT_PATH);
}
//// VISUALIZATION FUNCTION:
late() {
    all = sim.subpopulations.individuals;
    output_str = "G"; // Seperator between generations.
    for (ind in all) {
        if (ind.color == "")  // Sentinal in case ind.color is not assigned.
            // Change if you want a different default color.
            ind.color = "blue";
        ind_colors = color2rgb(ind.color);
        hex_x = format("%.3x ", asInteger(ind.x * 4095 + 0.5));
        hex_y = format("%.3x ", asInteger(ind.y * 4095 + 0.5));
        hex_r = format("%.2x ", asInteger(255 * ind_colors[0]));
        hex_g = format("%.2x ", asInteger(255 * ind_colors[1]));
        hex_b = format("%.2x",  asInteger(255 * ind_colors[2]));
        output_str = output_str + "\n" +  hex_x + hex_y + hex_r + hex_g + hex_b;
    }
    writeFile(OUTPUT_PATH, output_str, T);
}
```

##### OPTION 2. For slim code that uses colors that are hex codes, such as "#FFFF00":
```C
//// SET OUTPUT PATH FOR VISUALIZATION FUNCTION:
1 early() {
    defineConstant("OUTPUT_PATH", getwd() + "/slim_movie");
    deleteFile(OUTPUT_PATH);
}
//// VISUALIZATION FUNCTION:
late() {
    all = sim.subpopulations.individuals;
    output_str = "G"; // Seperator between generations.
    for (ind in all) {
        if (ind.color == "")  // Sentinal in case ind.color is not assigned.
            // Change if you want a different default color.
            ind.color = "#0000FF";
        hex_x = format("%.3x ", asInteger(ind.x * 4095 + 0.5));
        hex_y = format("%.3x ", asInteger(ind.y * 4095 + 0.5));
        r = substr(ind.color, 1, 2) + " ";
        g = substr(ind.color, 3, 4) + " ";
        b = substr(ind.color, 5, 6);
        output_str = output_str + "\n" +  hex_x + hex_y + r + g + b;
    }
    writeFile(OUTPUT_PATH, output_str, T);
}
```
