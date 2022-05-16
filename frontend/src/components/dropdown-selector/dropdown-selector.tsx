import React from "react";

import Box from "@mui/material/Box";
import FormControl from "@mui/material/FormControl";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import InputLabel from "@mui/material/InputLabel";


interface DropdownSelectorProps {
  menuItems: string[],
  updateWhenSelect: (item: string) => void,
  selectorName?: string,
  selectedItem: string,
}

const DropdownSelector = ({ menuItems, updateWhenSelect, selectorName, selectedItem }: DropdownSelectorProps) => (
  <Box sx={{ minWidth: 120 }}>
    <FormControl fullWidth>
      <InputLabel id={`${selectorName}-select-label`}>{ selectorName }</InputLabel>
      <Select
        labelId={`selector_${selectorName}`}
        id={`selector_${selectorName}`}
        value={selectedItem}
        label={selectorName?? ''}
        onChange={(event: SelectChangeEvent) => {
          updateWhenSelect(event.target.value as string);
        }}
      >
        {menuItems.map(menuItem => (
          <MenuItem value={menuItem}>{ menuItem }</MenuItem>
        ))}
      </Select>
    </FormControl>
  </Box>
) 

export default DropdownSelector