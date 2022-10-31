# :athletic_shoe: How to run this frontend code
This project using **React Native** with development on macOS and target on iOS.

## Run instructions for Android:
   - Have an Android emulator running (quickest way to get started), or a device connected.
   - cd "Frontend/ddlReminder" && npx react-native run-android
  
## Run instructions for  iOS:
   - cd "/Frontend/ddlReminder" && npx react-native run-ios
    -- or --
   - Open ddlReminder/ios/ddlReminder.xcworkspace in Xcode or run "xed -b ios"
   - Hit the Run button


# :memo: Others
## React vs. React Native
| |React|React Native|
|-|-----|------------|
|**What is**|A **front-end** development library. Also known as *ReactJs*, a JS library for building the UIs for **web apps**|A native **mobile** development library. To build **mobile UI** declarative components using only JS. React Native utilizes the base abstraction of ReactJs, but only the library components are distinct.|
|**Difference**|1. Uses virtual DOM to create UX<br>2. Integrate React library in HTML page<br> 3. Execute apps ont he client-side while rendering on the server-side<br> 4. Must learn and understand JS<br> 5. Render HTML-like (JSX) components with \<p>, \<div>, \<h1> <br> 6. Uses local storage to store and manage data|1. Uses APIs to render UI components<br> 2. Mast have development environment like Android Studio and Xcode<br> 3. Can integrate native codes with JAva, Swift, Objective-C<br>4. Combines JAva, Objective-C, Objective-C++ and C++ code<br> 5. Render native components like \<view>, \<text>, \<images> <br> 6. Uses asyncStorage by default|
|**Pros**|Easy learning curve<br> Reusable components<br>Virtual DOM|Easy to learn and implement<br> Reusable code<br>Fewer errors|
|**Cons**|Few native modules|Long load time|

## React Native Core Components
|REACT NATIVE UI COMPONENT|ANDROID VIEW|IOS VIEW|WEB ANALOG|DESCRIPTION|
|-------------------------|------------|--------|----------|-----------|
|`<View>`|`<ViewGroup>`|`<UIView>`|A non-scrolling `<div>`|A container that supports layout with flexbox, style, some touch handling, and accessibility controls|
|`<Text>`|`<TextView>`|`<UITextView>`|`<p>`|Displays, styles, and nests strings of text and even handles touch events|
|`<Image>`|`<ImageView>`|`<UIImageView>`|`<img>`|Displays different types of images|
|`<ScrollView>`|`<ScrollView>`|`<UIScrollView>`|`<div>`|A generic scrolling container that can contain multiple components and views|
|`<TextInput>`|`<EditText>`|`<UITextField>`|`<input type="text">`|Allows the user to enter text|


![React Native Components](/img/ReactNativeComponents.png)



# :smiley_cat: Something that makes my life easier

## ANTD:ant: and Styled-components
- [ANTD](https://rn.mobile.ant.design/docs/react/introduce-cn): pre-defined UI library, save time to style UI components.
- [Styled-components](https://styled-components.com): able to use css style inside js/ts file, easy to structure and modify style.

## Short keys :rocket:
Install dependence "**ES7+ React/Redux/React-Native snippets**" in VS Code. After create <u>a new components</u>,
- `rafc` get *Creates a **React Arrow Function Component** with ES7 module system (ES7+ React/Redux/React-Native snippets)*
```tsx
import React from 'react'

export const Home = () => {
  return (
    <div>Home</div>
  )
}
```
- `rafce` get *Creates a **React Arrow Function Export Component** with ES7 module system (ES7+ React/Redux/React-Native snippets)*
```tsx
import React from 'react'

const Home = () => {
  return (
    <div>Home</div>
  )
}

export default Home
```
- `rafcp` get *Creates a **React Arrow Function Component With PropTypes** with ES7 module syste (ES7+ React/Redux/React-Native snippets)*
```tsx
import React from 'react'
import PropTypes from 'prop-types'

const Home = props => {
  return (
    <div>Home</div>
  )
}

Home.propTypes = {}

export default Home
```
:warning: When using react native, replace all the default `<div>` into `<Text>`, otherwise will got compile error.