import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import ThemeProvider from '@mui/material/styles/ThemeProvider';
import { Route, Routes } from 'react-router-dom';
import DataPanelPage from './page/data-panal-page';
import createTheme from '@mui/material/styles/createTheme';
import { Panels, Population_Panel_Options, Scenarios } from './meta-data';


export const DataDisplayContext = React.createContext<{
  // currentPanel: Panels
  openOptionsDrawer: boolean,
  selectedScenario: string,
  displayOptions: any,
  setScenario: (scenario: string) => void,
  setOpenOptionsDrawer:(isOpened: boolean) => void,
  setDisplayOptions: (options: any) => void
}>({ 
  // currentPanel: Panels.POPULATION_PANEL,
  openOptionsDrawer: true,
  selectedScenario: '',
  displayOptions: null,
  setScenario: () => {},
  setOpenOptionsDrawer: () => {},
  setDisplayOptions: () => {}
})

function App() {
  const [openDrawer, setOpenDrawer] = useState(true) 
  const [selectedScenario, setSeletedScenario] = useState<string>(Scenarios.POPULATION_ANALYSIS)
  const [displayDataOptions, setDisplayDataOptions] = useState<any>(Object.values(Population_Panel_Options))

  const theme = React.useMemo(
    () =>
      createTheme({
        palette: {
          mode: 'light',
        },
      }),
    [],
  );

  return (
    <ThemeProvider theme={theme}>
      <DataDisplayContext.Provider value={{
        // currentPanel: Panels.POPULATION_PANEL,
        openOptionsDrawer: openDrawer,
        selectedScenario: selectedScenario,
        displayOptions: displayDataOptions,
        setScenario: (scenario: string) => {setSeletedScenario(scenario)},
        setOpenOptionsDrawer: (isOpened: boolean) => {setOpenDrawer(isOpened)},
        setDisplayOptions: (options: any) => {setDisplayDataOptions(options)}
      }}>
        <Routes>
          <Route key='datapanel' path='/' element={<DataPanelPage />}/>
        </Routes>
      </DataDisplayContext.Provider>
    </ThemeProvider>
  );
}

export default App;
