import * as React from 'react';
import Box from '@mui/material/Box';
import Slider from '@mui/material/Slider';

const minDistance = 0.01;

interface SliderComponentProps {
  startEndDate: number[],
  selectedStartEndDate: number[],
  updateSelectedStartEndDate: (updatedStartEndDate: number[]) => void
}

const SliderComponent = ({ startEndDate, selectedStartEndDate, updateSelectedStartEndDate }: SliderComponentProps) => {
  // const [value1, setValue1] = React.useState<number[]>([20, 37]);
  // console.log('startEndDate222')
  // console.log(startEndDate)

  const handleChange1 = (
    event: Event,
    newValue: number | number[],
    activeThumb: number,
  ) => {
    if (!Array.isArray(newValue)) {
      return;
    }

    if (activeThumb === 0) {
      updateSelectedStartEndDate([Math.min(newValue[0], selectedStartEndDate[1] - minDistance), selectedStartEndDate[1]]);
    } else {
      updateSelectedStartEndDate([selectedStartEndDate[0], Math.max(newValue[1], selectedStartEndDate[0] + minDistance)]);
    }
  };

  return (
    <Box sx={{ width: 300 }}>
      <Slider
        getAriaLabel={() => 'Minimum distance'}
        value={selectedStartEndDate}
        onChange={handleChange1}
        valueLabelDisplay="auto"
        min={startEndDate[0]}
        max={startEndDate[1]}
        // getAriaValueText={valuetext}
        disableSwap
      />
    </Box>
  );
}

export default SliderComponent