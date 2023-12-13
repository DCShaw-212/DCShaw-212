//
//  TrailerTires.swift
//  CDL_Pretrip_Flashcards
//
//  Created by Dustin Shaw on 8/28/22.
//

import SwiftUI

struct TrailerTires: View {
    
    
    private let colors: [Color] = [.gray, .white]
    private var question : String =  "Items To be Checked: \n Tires \n Inflation \nDepth \nCondition"
    private var answer : String = "\n Tire Depth - 2/32 of an inch. Tread Worn Evenly. \n Tire Condition - No abrasions bulges or cuts. \nTire Inflation - Checked with a tire pressure gauge."
    
    var body: some View {
        
        VStack{
            TabView{
                ForEach(colors, id: \.self) { color in
                    ZStack{
                        color.ignoresSafeArea()
                        
                        VStack{
                           
                        Text("Trailer")
                            .padding()
                            .background(.orange)
                            .font(.title2)
                            .foregroundColor(.black)
                           
                            Image("tires").resizable()
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
                            
                            NavigationLink(destination:TrailerRims()){
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

struct TrailerTires_Previews: PreviewProvider {
    static var previews: some View {
        TrailerTires()
    }
}
