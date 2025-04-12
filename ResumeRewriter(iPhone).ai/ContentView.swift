//
//  ContentView.swift
//  ResumeRewriter(iPhone).ai
//
//  Created by Sherkeem Duprey on 4/11/25.
//

import PDFKit
import SwiftUI
import UniformTypeIdentifiers

struct ContentView: View {
    @State private var jobDesc = ""
    @State private var showFileImporter = false
    var onTemplatesDirectoryPicked: (URL) -> Void = { _ in }

    var body: some View {
        VStack {
            Text("Resume Rewriter")
                .font(.headline)
                .padding()
            Button {
                showFileImporter = true
            } label: {
                Label("Upload resume (.pdf)", systemImage: "folder.circle")
            }
            .fileImporter(
                isPresented: $showFileImporter,
                allowedContentTypes: [.pdf]
            ) { result in
                switch result {
                case .success(let directory):
                    let gotAccess = directory.startAccessingSecurityScopedResource()
                    if !gotAccess { return }
                    onTemplatesDirectoryPicked(directory)
                    directory.stopAccessingSecurityScopedResource()
                case .failure(let error):
                    print(error)
                }
            }

            TextField(
                "Enter job description",
                text: $jobDesc
            )
            .textFieldStyle(RoundedBorderTextFieldStyle())
            .padding()
            
            Button(action: rewrite) {
                Text("Rewrite!")
            }
        }
    }
    func rewrite() {
        // your logic here, e.g., modify some @State variable
        print("Rewriting...")
    }
}

#Preview {
    ContentView()
}

/*
 struct PickTemplatesDirectoryButton: View {
      @State private var showFileImporter = false
      var onTemplatesDirectoryPicked: (URL) -> Void

      var body: some View {
          Button {
              showFileImporter = true
          } label: {
              Label("Choose templates directory", systemImage: "folder.circle")
          }
          .fileImporter(
              isPresented: $showFileImporter,
              allowedContentTypes: [.directory]
          ) { result in
               switch result {
               case .success(let directory):
                   // gain access to the directory
                   let gotAccess = directory.startAccessingSecurityScopedResource()
                   if !gotAccess { return }
                   // access the directory URL
                   // (read templates in the directory, make a bookmark, etc.)
                   onTemplatesDirectoryPicked(directory)
                   // release access
                   directory.stopAccessingSecurityScopedResource()
               case .failure(let error):
                   // handle error
                   print(error)
               }
          }
      }
  }
 */
