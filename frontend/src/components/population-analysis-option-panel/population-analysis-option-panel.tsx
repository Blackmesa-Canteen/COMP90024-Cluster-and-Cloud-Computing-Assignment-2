import React, { useContext, useState } from "react";

import { Scenarios } from "../../meta-data";

import CheckBox from "../check-box/check-box";
import Box from "@mui/material/Box";
import { DataDisplayContext } from "../../App";
import Stack from "@mui/material/Stack";
import { Button,  Step, StepContent, StepLabel, Typography } from "@mui/material";
import LooksTwoIcon from '@mui/icons-material/LooksTwo';
import Looks3Icon from '@mui/icons-material/Looks3';



const PopulationAnalysisOptionPanel = () => {
  const { setDisplayOptions, setScenario, displayOptions } = useContext(DataDisplayContext)
  const [selectedDataSet, setSelectedDataSet] = useState(displayOptions as string[])

  const deleteSelectedDataset = (datasetToDelete: string) => {
    setSelectedDataSet(selectedDataSet.filter(sds => sds !== datasetToDelete))
  }

  const addSelestedDataset = (datasetToAdd: string) => {
    if (!selectedDataSet.includes(datasetToAdd)) {
      setSelectedDataSet([...selectedDataSet, datasetToAdd])
    }
  }

  const handleSubmit = () => {
    setDisplayOptions(selectedDataSet)
    setScenario(Scenarios.POPULATION_ANALYSIS)
  }
  

  return (
    <>
      <Step key={2}>
        <StepLabel>
          <Stack direction='row' spacing={2}>
            <LooksTwoIcon sx = {{color:"#2196f3"}} />
            <Typography variant='body1' sx={{ fontWeight: '600' }}>
              Options
            </Typography>
          </Stack>
        </StepLabel>
        <StepContent>
          <Box sx={{padding: '20px'}}>
            <CheckBox 
              menuItems={selectedDataSet} 
              deleteDataSet={deleteSelectedDataset} 
              addDataSet={addSelestedDataset}
            />
          </Box>
        </StepContent>
      </Step>
      <Step key={3}>
        <StepLabel>
          <Stack direction='row' spacing={2}>
            <Looks3Icon sx = {{color:"#2196f3"}} />
            <Typography variant='body1' sx={{ fontWeight: '600' }}>
              LoadData
            </Typography>
          </Stack>
        </StepLabel>
        <StepContent>
          <Box sx={{ width: '100%', height: '100%', display: 'flex', padding: '20px', alignItems: 'center' }}>
            <Button variant="contained" onClick={() => {handleSubmit()}}>
              Confirm
            </Button>
          </Box>
        </StepContent>
      </Step>
    </>
  )
}

export default PopulationAnalysisOptionPanel