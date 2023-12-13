//
//  RearMudFlaps.swift
//  CDL_Pretrip_Flashcards
//
//  Created by Dustin Shaw on 8/28/22.
//

import SwiftUI

struct RearMudFlaps: View {
    
    private let colors: [Color] = [.gray, .white]
    private var question : String =  "Items To be Checked: \n Splash Guards \n Mud Falps "
    private var answer : String = "\n Secure. \n Not ripped, torn, or dragging the ground."
    
    var body: some View {
        
        
         VStack{
             TabView{
                 ForEach(colors, id: \.self) { color in
                     ZStack{
                         color.ignoresSafeArea()
                         
                         VStack{
                            
                         Text("Rear Truck \n Splash Guards")
                             .padding()
                             .background(.orange)
                             .font(.title2)
                             .foregroundColor(.black)
                            
                             Image("truckMudFlaps").resizable()
                                 .aspectRatio(contentMode: .fit)
                                 .frame(width: 200, height: 200, alignment: .center)
                             
                             if (color.description == "gray")
                             {
                                 
                                 Text("\(question)")
                                     .padding()
                                     .font(.title3)
                                     .foregroundColor(.black)
                                     .background(.white)
                                 Spacer()
                             }
                             else{
                                 Text("Description:")
                                     .padding()
                                     .font(.title3)
                                     .foregroundColor(.white)
                                     .background(.black)
                                 Text("\(answer)")
                                     .padding()
                                     .font(.headline)
                                     .foregroundColor(.white)
                                     .background(.black)
                                 Spacer()
                             }
                             
                             NavigationLink(destination:RearTruckLights()){
                                         Text("Next")
                                             .padding()
                                             .font(.title)
                                             .background(.orange)
                                             .foregroundColor(.black)
                                             .cornerRadius(60)
                                     }
                         
                             Spacer()
                         }
                     }
                     .ignoresSafeArea()
                     
                 }
             }
             .tabViewStyle(.page)
             .indexViewStyle(.page(backgroundDisplayMode: .interactive))
         }
       
    }
}

struct RearMudFlaps_Previews: PreviewProvider {
    static var previews: some View {
        RearMudFlaps()
    }
}
