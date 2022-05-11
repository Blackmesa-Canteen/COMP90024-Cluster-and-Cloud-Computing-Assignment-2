import React from "react";

import FormGroup from "@mui/material/FormGroup";
import Stack from "@mui/material/Stack";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from '@mui/material/Checkbox';
import { Population_Panel_Options } from "../../meta-data";

interface CheckBoxProps {
  menuItems: string[]
  addDataSet: (dsKey: string) => void
  deleteDataSet: (dsKey: string) => void
}

const CheckBox = ({ menuItems, addDataSet, deleteDataSet }: CheckBoxProps) => {
  return (
  <FormGroup >
    {/* <Stack direction='column'> */}
      {Object.values(Population_Panel_Options).map(value => (
        // <Stack direction='row' spacing={2}>
          <FormControlLabel 
            onChange={(e: any) => {
              // console.log('select=>')
              if (e.target.checked) {
                addDataSet(value)
              }
              else {
                deleteDataSet(value)
              }
            }} 
            control={<Checkbox checked={menuItems.includes(value)} defaultChecked/>} 
            label={value} 
          />
        // </Stack>
      ))}
    {/* </Stack> */}
  </FormGroup>)
}

export default CheckBox;