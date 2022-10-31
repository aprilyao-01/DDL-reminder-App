import React from 'react'
import { Text } from 'react-native'
import { Button, Icon, WhiteSpace, WingBlank } from '@ant-design/react-native'
import { MyTitle, StyledText, StyledView } from '../appStyles'


const Home = () => {
  return (
    <WingBlank>
        <Text>Home</Text>
        <Button type="primary">primary</Button>
        <WhiteSpace />
        <Button type="warning">warning</Button>
        <MyTitle>Hello World!</MyTitle>
        <StyledView>
        <StyledText>Hello again!</StyledText>
      </StyledView>
    </WingBlank>
    
  )
}

export default Home