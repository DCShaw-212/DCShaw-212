//
//  RearTire.swift
//  CDL_Pretrip_Flashcards
//
//  Created by Dustin Shaw on 8/28/22.
//

import SwiftUI

struct RearTire: View {
    
    
    private let colors: [Color] = [.gray, .white]
    private var question : String =  "Items To be Checked: \n Tire Inflation \n Tire Depth \n Tire Condition"
    private var answer : String = "\n Tire Depth - No less thand 2/32 inch. \n Tire Inflation - Checked with tire pressure gauge. \n Filled to manufacturer specification.  \n Tire Condition - No abrasion cuts or tears. "
    
    var body: some View {
        
        
        VStack{
            TabView{
                ForEach(colors, id: \.self) { color in
                    ZStack{
                        color.ignoresSafeArea()
                        
                        VStack{
                           
                        Text("Rear Tires")
                            .padding()
                            .background(.orange)
                            .font(.title2)
                            .foregroundColor(.black)
                           
                            Image("tire").resizable()
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
                            
                            NavigationLink(destination:RearRims()){
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

struct RearTire_Previews: PreviewProvider {
    static var previews: some View {
        RearTire()
    }
}
