import React, { useContext, useMemo, useState } from "react";

import DropdownSelector from "../dropdown-selector/dropdown-selector";
import { Population_Panel_Options, Scenarios } from "../../meta-data";

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
import LockdownInfluenceAnalysisOptionPanel from "../lockdown-influence-analysis-option-panel/lockdown-influence-analysis-option-panel";
import HousePriceOptionsPanel from "../house-price-options-panel/house-price-options-panel";
import TwitterAnalysisOptionPanel from "../twitter-analysis-option-panel/twitter-analysis-option-panel";

const LeftDrawer = () => {
  const { openOptionsDrawer, setOpenOptionsDrawer, selectedScenario, setScenario, setDisplayOptions } = useContext(DataDisplayContext)
  const [ currentSelectedScenario, setCurrentSelectedScenario] = useState(selectedScenario)

  const optionsPanel = useMemo(() => {
    switch(currentSelectedScenario) {
      case Scenarios.POPULATION_ANALYSIS:
        return <PopulationAnalysisOptionPanel/>
      case Scenarios.TOP_10_LANGUAGE_ANALYSIS:
        return <Top10LanguageAnalysisOptionsPanel/>
      case Scenarios.HOUSE_PRICE_ANALYSIS:
        return <HousePriceOptionsPanel />
      case Scenarios.LOCK_DOWN_INFLUENCE_ANALYSIS:
        return <LockdownInfluenceAnalysisOptionPanel/>
      case Scenarios.TWITTER_ANALYSIS:
        return <TwitterAnalysisOptionPanel />
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
                updateWhenSelect={(scenario: string) => {
                  setCurrentSelectedScenario(scenario)
                  setScenario(scenario)
                  switch(scenario) {
                    case Scenarios.POPULATION_ANALYSIS:
                      setDisplayOptions(Object.values(Population_Panel_Options))
                      break;
                    case Scenarios.TOP_10_LANGUAGE_ANALYSIS:
                      // setDisplayOptions([1,2])
                      break;
                    case Scenarios.HOUSE_PRICE_ANALYSIS:
                      break;
                    case Scenarios.LOCK_DOWN_INFLUENCE_ANALYSIS:
                      break;
                  }
                }}
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