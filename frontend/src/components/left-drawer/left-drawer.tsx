import React, { useContext, useMemo, useState } from "react";

import DropdownSelector from "../dropdown-selector/dropdown-selector";
import { Scenarios } from "../../meta-data";

import Box from "@mui/material/Box";
import Drawer from "@mui/material/Drawer/Drawer";
import { DataDisplayContext } from "../../App";
import Stack from "@mui/material/Stack";
import { Button, IconButton, Step, StepContent, StepLabel, Stepper, Typography } from "@mui/material";
import MenuIcon from '@mui/icons-material/Menu';
import LooksOneIcon from '@mui/icons-material/LooksOne';
import LooksTwoIcon from '@mui/icons-material/LooksTwo';
import PopulationAnalysisOptionPanel from "../population-analysis-option-panel/population-analysis-option-panel";
import Looks3Icon from '@mui/icons-material/Looks3';
import Top10LanguageAnalysisOptionsPanel from "../top10language-analysis-options-panel/top10language-analysis-options-panel";

const LeftDrawer = () => {
  const { openOptionsDrawer, setOpenOptionsDrawer, selectedScenario } = useContext(DataDisplayContext)
  const [ currentSelectedScenario, setCurrentSelectedScenario] = useState(selectedScenario)

  const optionsPanel = useMemo(() => {
    switch(currentSelectedScenario) {
      case Scenarios.POPULATION_ANALYSIS:
        return <PopulationAnalysisOptionPanel/>
      case Scenarios.TOP_10_LANGUAGE_ANALYSIS:
        return <Top10LanguageAnalysisOptionsPanel/>
    }
  }, [currentSelectedScenario])

  return (
    openOptionsDrawer?
    (<Drawer anchor="left" open={openOptionsDrawer} onClose={() => {setOpenOptionsDrawer(false)}}>
      <Stack sx={{ minWidth: '220px', margin: '20px', marginTop: '50px', }}>
      {/* <Stepper  orientation="vertical"> */}
        <Step key={1}>
          <StepLabel>
            <Stack direction='row' spacing={2}>
              <LooksOneIcon sx = {{color:"#2196f3"}} />
              <Typography variant='body1' sx={{ fontWeight: '600' }}>
              Select an scenario to analyze
              </Typography>
            </Stack>
          </StepLabel>
          <StepContent>
            <Box sx={{padding: '20px'}}>
              <DropdownSelector 
                menuItems={Object.values(Scenarios)}
                updateWhenSelect={(scenario: string) => setCurrentSelectedScenario(scenario)}
                selectedItem={currentSelectedScenario}
              />
            </Box>
          </StepContent>
        </Step>
        {optionsPanel}
      {/* </Stepper> */}
      </Stack>
    </Drawer>)
    :
    (<IconButton id='openDrawerButton' onClick={() => {setOpenOptionsDrawer(true)}} sx={{ margin: '10px' }}>
      <MenuIcon/>
    </IconButton>)
  )
}

export default LeftDrawer;